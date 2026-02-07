import requests
from config import VIRUSTOTAL_API_KEY


def scan_url_virustotal(url_to_scan: str):
    """
    Checks URL reputation using VirusTotal
    """

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    # Step 1: Submit URL for analysis
    scan_url = "https://www.virustotal.com/api/v3/urls"

    try:
        response = requests.post(scan_url, headers=headers, data={"url": url_to_scan})
        analysis_id = response.json()["data"]["id"]

        # Step 2: Get analysis results
        result_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        result = requests.get(result_url, headers=headers).json()

        stats = result["data"]["attributes"]["stats"]

        malicious = stats["malicious"]
        suspicious = stats["suspicious"]
        harmless = stats["harmless"]

        if malicious > 5:
            risk = "High"
        elif malicious > 0:
            risk = "Medium"
        else:
            risk = "Low"

        return {
            "malicious": malicious,
            "suspicious": suspicious,
            "harmless": harmless,
            "risk_level": risk
        }

    except Exception as e:
        print("VirusTotal lookup failed:", e)
        return None
