import requests, json, os, sys

KEY = os.environ.get("API_KEY", "").strip()
print("key length:", len(KEY))

URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
r = requests.get(URL, params={"api-key": KEY, "format": "json", "limit": 1000}, timeout=60)
print("status:", r.status_code)
print(r.text[:300])

records = r.json().get("records", []) if r.ok else []
if not records:
    sys.exit("No records received")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False)
