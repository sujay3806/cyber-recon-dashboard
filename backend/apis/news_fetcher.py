import requests
from config import NEWS_API_KEY


def get_cyber_news():
    """
    Fetches latest cybersecurity news articles
    """

    url = "https://newsapi.org/v2/everything"

    params = {
    "q": '"cyber attack" OR "data breach" OR ransomware OR malware OR vulnerability OR exploit OR CVE',
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 5,
    "domains": "bleepingcomputer.com,theregister.com,securityweek.com,threatpost.com,zdnet.com",
    "apiKey": NEWS_API_KEY
}


    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        articles = []

        for item in data.get("articles", []):
            articles.append({
                "title": item["title"],
                "source": item["source"]["name"],
                "url": item["url"],
                "published": item["publishedAt"]
            })

        return articles

    except Exception as e:
        print("News fetch failed:", e)
        return []
