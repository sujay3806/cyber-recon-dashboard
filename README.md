# 🔐 Cyber Recon Dashboard

A full-stack **Cybersecurity Intelligence & Reconnaissance Platform** that combines port scanning, vulnerability intelligence, IP reputation, malware analysis, and live cyber threat news into one interactive dashboard.

Built as a **learning + security research project** demonstrating how real-world recon and threat intelligence systems work.

---

## 🚀 Features

| Feature                      | Description                                   |
| ---------------------------- | --------------------------------------------- |
| ⚡ Async Port Scanner         | Scans ports using asyncio for high speed      |
| 🖥 OS Fingerprinting         | Detects OS using TTL values                   |
| 🏴 Banner Grabbing           | Identifies running services                   |
| 🚨 CVE Vulnerability Mapping | Links services to known vulnerabilities       |
| 🌍 IP Reputation Check       | Checks if IP is malicious (AbuseIPDB)         |
| 🦠 URL Malware Scan          | Scans URLs using VirusTotal                   |
| 📰 Cybersecurity News        | Live threat news carousel                     |
| 🧪 Demo Mode                 | Safe simulated scanning for public deployment |
| ⬇ Local Scanner Download     | Users can scan their own machine legally      |
| 🛡 Security Protections      | Rate limiting + scan restrictions             |

---

## 🧠 Tech Stack

### Backend

* **FastAPI** – High-performance API framework
* **Asyncio** – Concurrent port scanning
* **Python Sockets** – TCP connection scanning
* **SlowAPI** – Rate limiting
* **Requests** – External API calls

### Frontend

* **React** – Interactive UI
* **Tailwind CSS** – Modern styling
* **Framer Motion** – Smooth animations
* **Axios** – API communication

---

## 🌐 APIs Used

| API                                   | Purpose                  |
| ------------------------------------- | ------------------------ |
| NVD (National Vulnerability Database) | CVE vulnerability lookup |
| AbuseIPDB                             | IP reputation scoring    |
| VirusTotal                            | Malware URL analysis     |
| NewsAPI                               | Cybersecurity news feed  |

---

## 🧩 How It Works (User Flow)

1. User opens dashboard
2. Enters IP & port range
3. Backend validates target
4. Async scanner checks ports
5. Banner grabbing identifies service
6. CVE API maps vulnerabilities
7. Results shown in table
8. User can also check IP reputation or scan a URL
9. News panel updates automatically

---

## ⚙ Installation (Backend)

```bash
git clone https://github.com/YOUR_USERNAME/cyber-recon-dashboard.git
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## ⚙ Installation (Frontend)

```bash
cd backend/frontend
npm install
npm start
```

---

## 🔑 Environment Variables (.env)

```
NVD_API_KEY=your_key_here
ABUSEIPDB_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

---

## 🧪 Demo Mode

Public deployment runs in **safe demo mode**:

* Real scanning disabled for external IPs
* Simulated results shown

To scan your own PC → download the **Local Scanner Tool** from the dashboard.

---

## 🛡 Legal Notice

This tool is for **educational and authorized security testing only**.
Do NOT scan systems without permission.

---

## 📚 What You Learn From This Project

* Async networking
* Threat intelligence integration
* API security
* WebSockets & real-time UI
* Vulnerability management concepts

---

## 🔮 Future Improvements

* Real-time WebSocket scan updates
* Advanced OS fingerprinting
* CVSS scoring visualization
* User accounts & history
* Docker deployment

---

## 👨‍💻 Author

**Sujay Chawda**
