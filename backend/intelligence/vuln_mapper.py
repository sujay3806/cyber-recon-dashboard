# vuln_mapper.py

from apis.cve_lookup import search_cve

# This is a SMALL offline vulnerability database
# Later we can replace with NVD API

VULN_DB = {
    "OpenSSH_7": {
        "cves": ["CVE-2016-0777"],
        "severity": "HIGH"
    },
    "Apache/2.4.49": {
        "cves": ["CVE-2021-41773"],
        "severity": "CRITICAL"
    },
    "vsFTPd 2.3.4": {
        "cves": ["CVE-2011-2523"],
        "severity": "CRITICAL"
    }
}

def parse_banner(banner: str):
    """
    Attempts to extract product name and version from banner string.
    Example: 'Apache/2.4.49' → ('Apache', '2.4.49')
    """
    try:
        parts = banner.split("/")
        product = parts[0]
        version = parts[1].split()[0]
        return product, version
    except:
        return None, None
    
    
def check_vulnerabilities(banner: str):
    """
    Checks if banner matches known vulnerable software.
    Returns CVE list and severity if found.
    """

    if not banner:
        return None

    product,version = parse_banner(banner)
    
    if not product or not version:
        return None

    return search_cve(product, version)
    
    for software, data in VULN_DB.items():
        if software.lower() in banner.lower():
            return data

    return None

