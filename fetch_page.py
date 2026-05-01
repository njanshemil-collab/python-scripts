import requests as rq
fet=rq.get("https://example.com")
print("here - ",fet.status_code)