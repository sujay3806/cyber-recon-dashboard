import asyncio
from config import SCAN_TIMEOUT,MAX_CONCURRENT_CONNECTIONS
from scanners.banner_grabber import grab_banner
from intelligence.vuln_mapper import check_vulnerabilities

semaphore = asyncio.Semaphore(MAX_CONCURRENT_CONNECTIONS)

async def scan_port(ip: str, port:int):
    
    async with semaphore:
        try:
            reader,writer = await asyncio.wait_for(
                asyncio.open_connection(ip,port),
                timeout=SCAN_TIMEOUT
            )
            # TEMP TEST — simulate vulnerable service

            banner = await grab_banner(reader,writer)
                
            vuln_info = check_vulnerabilities(banner)
            
            writer.close()
            await writer.wait_closed()
                
            return{
                "port":port,
                "status":"OPEN",
                "banner": banner,
                 "vulnerabilities": vuln_info
            }
        except:
            return{
                "port": port,
                "status": "CLOSED",
                "banner": None
            }
            
async def run_port_scan(ip: str, start_port: int, end_port: int):
    tasks=[]
    
    for port in range (start_port, end_port+1):
        tasks.append(scan_port(ip,port))
        
    results = await asyncio.gather(*tasks)
        
    return results 

