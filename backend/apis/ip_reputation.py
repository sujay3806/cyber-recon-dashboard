import requests
from config import ABUSEIPDB_API_KEY


def check_ip_reputation(ip: str):
    """
    Checks IP reputation using AbuseIPDB API
    """

    url = "https://api.abuseipdb.com/api/v2/check"

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        data = response.json()["data"]

        score = data["abuseConfidenceScore"]
        reports = data["totalReports"]
        last_reported = data["lastReportedAt"]

        # Simple risk classification
        if score >= 75:
            risk = "High"
        elif score >= 30:
            risk = "Medium"
        else:
            risk = "Low"

        return {
            "confidence_score": score,
            "reports": reports,
            "last_reported": last_reported,
            "risk_level": risk
        }

    except Exception as e:
        print("IP reputation check failed:", e)
        return None
