🛡️ Cyber Recon & Threat Intelligence Dashboard

A full-stack Cybersecurity Reconnaissance and Intelligence Platform that combines:

Network scanning

OS fingerprinting

Service banner detection

CVE vulnerability intelligence

IP reputation analysis

Malware URL scanning

Live cybersecurity news

Built using FastAPI + Async Python + Threat Intelligence APIs.

🚀 Features
Module	Description
⚡ Async Port Scanner	High-performance port scanning using asyncio
🖥 OS Detection	TTL-based OS fingerprinting
🏷 Banner Grabbing	Identifies services running on open ports
🧨 CVE Mapping	Matches services to vulnerabilities via NVD
🌍 IP Reputation	Checks abuse history using AbuseIPDB
🦠 Malware URL Scan	URL threat detection via VirusTotal
📰 Threat News Feed	Real-time cybersecurity headlines
🔒 Safe Scanning Policy	Prevents scanning public/external systems
⏱ Rate Limiting	Prevents API abuse
⚠️ Legal Notice

This tool is for educational and authorized security testing only.
Do not scan systems without permission.

🧠 How It Works
User Request → Backend Scanner → Threat Intelligence APIs → Results Dashboard


Flow:

Target is validated (only private/local IPs allowed)

Ports are scanned asynchronously

Services are identified

Vulnerabilities are fetched from NVD

IP reputation & malware checks are performed

Cyber threat news is displayed

🛠 Installation
1️⃣ Clone repository
git clone https://github.com/yourusername/cyber-recon-dashboard.git
cd cyber-recon-dashboard/backend

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Setup environment variables

Create .env inside backend/:

NVD_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
ABUSEIPDB_API_KEY=your_key_here
NEWS_API_KEY=your_key_here

4️⃣ Run server
uvicorn main:app --reload


Open:

http://127.0.0.1:8000

📡 API Endpoints
Endpoint	Function
/scan	Scan target IP ports
/news	Latest cybersecurity news
/ip-reputation	Check IP threat history
/scan-url	Malware URL analysis
/legal	Legal disclaimer
🔐 Security Protections

To make the system safe for public deployment:

Only private/local IP scanning allowed

Port range limited

Rate limiting enabled

Legal notice included

🐞 Common Errors & Fixes
Issue	Fix
NVD KEY: None	Check .env variable name
CVEs not showing	Banner parsing issue
403 scanning error	Target IP is public
429 error	Too many requests (rate limit)
VirusTotal returns empty	URL not scanned before
📌 Tech Stack

FastAPI

Asyncio

SlowAPI (Rate limiting)

NVD API

AbuseIPDB

VirusTotal

NewsAPI

🎯 Future Enhancements

Interactive dashboard UI

User authentication

Historical scan logs

Advanced OS fingerprinting

👨‍💻 Author

Cybersecurity Recon & Intelligence Project
Built for learning, research, and demonstration.