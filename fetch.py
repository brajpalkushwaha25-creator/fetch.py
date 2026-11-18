import requests, json, os, sys

KEY = os.environ["API_KEY"]
URL = ("https://api.data.gov.in/resource/"
       "9ef84268-d588-465a-a308-a864a43d0070"
       f"?api-key={KEY}&format=json&limit=1000")

try:
    r = requests.get(URL, timeout=60)
    r.raise_for_status()
    records = r.json().get("records", [])
    if not records:
        sys.exit(0)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False)
except Exception as e:
    print("API down, purana data rakha:", e)
