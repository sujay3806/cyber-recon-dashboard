from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query
from scanners.async_port_scanner import run_port_scan
from scanners.os_fingerprint import detect_os
from apis.news_fetcher import get_cyber_news
from apis.ip_reputation import check_ip_reputation
from apis.virustotal_lookup import scan_url_virustotal
from security.scan_policy import is_safe_target
from fastapi import HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from fastapi import Request
import socket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os


app=FastAPI(title="Cyber_Recon_Dashboard_API")
# Path to React build folder
build_path = os.path.join(os.path.dirname(__file__), "build")

# Serve static files
if os.path.exists(build_path):
    app.mount("/static", StaticFiles(directory=os.path.join(build_path, "static")), name="static")

    @app.get("/")
    async def serve_react():
        return FileResponse(os.path.join(build_path, "index.html"))

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests. Please slow down."}
    )

@app.get("/scan")
@limiter.limit("5/minute")
async def scan_target(
    request: Request,
    ip: str = Query(..., description="Target IP or domain"),
    start_port: int = Query(1, description="Start port"),
    end_port: int = Query(100, description="End port")
):
    # Port range limit
    if end_port - start_port > 100:
        raise HTTPException(status_code=400, detail="Max 100 ports per scan")

    # Resolve domain to IP
    try:
        resolved_ip = socket.gethostbyname(ip)
    except:
        raise HTTPException(status_code=400, detail="Invalid hostname")

    # Safety restriction
    if not is_safe_target(resolved_ip):
        raise HTTPException(
            status_code=403,
            detail="Scanning external/public IPs is disabled."
        )

    os_guess = detect_os(resolved_ip)
    results = await run_port_scan(resolved_ip, start_port, end_port)

    return {
        "target": resolved_ip,
        "os_guess": os_guess,
        "range": f"{start_port}-{end_port}",
        "results": results
    }


@app.get("/news")
@limiter.limit("10/minute")
def news_feed(
    request: Request,
):
    """
    Returns latest cybersecurity news
    """
    articles = get_cyber_news()
    return {"news": articles}

@app.get("/ip-reputation")
@limiter.limit("10/minute")
def ip_reputation(
    request: Request,
    ip: str):
    """
    Returns reputation data for an IP
    """
    result = check_ip_reputation(ip)
    return {"ip": ip, "reputation": result}

@app.get("/scan-url")
@limiter.limit("5/minute")
def scan_url(
    request: Request,
    url: str):
    """
    Scans URL using VirusTotal
    """
    result = scan_url_virustotal(url)
    return {"url": url, "analysis": result}

@app.get("/legal")
def legal_notice():
    return {
        "notice": "This tool is for educational and authorized security testing only. Do not scan systems without permission."
    }

# Serve React static files
# ---------------- SERVE REACT FRONTEND ----------------

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "build/static")),
    name="static",
)

@app.get("/")
def serve_root():
    return FileResponse(os.path.join(BASE_DIR, "build/index.html"))

@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    return FileResponse(os.path.join(BASE_DIR, "build/index.html"))

