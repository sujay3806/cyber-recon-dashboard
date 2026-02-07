import requests
from config import NVD_API_KEY


def search_cve(product: str, version: str):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    # Broader search works better
    params = {
        "keywordSearch": product,
        "resultsPerPage": 5
    }

    headers = {
        "apiKey": NVD_API_KEY
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        
        print("STATUS:", response.status_code)
        print("RAW RESPONSE:", response.text[:1000])  # show first part

        data = response.json()

        vulnerabilities = []

        for item in data.get("vulnerabilities", []):
            cve_id = item["cve"]["id"]
            description = item["cve"]["descriptions"][0]["value"]

            metrics = item["cve"].get("metrics", {})
            severity = "Unknown"

            if "cvssMetricV31" in metrics:
                severity = metrics["cvssMetricV31"][0]["cvssData"]["baseSeverity"]

            vulnerabilities.append({
                "cve_id": cve_id,
                "severity": severity,
                "description": description[:120] + "..."
            })

        print("NVD returned CVEs:", len(vulnerabilities))
        return vulnerabilities if vulnerabilities else None

    except Exception as e:
        print("CVE lookup failed:", e)
        return None
