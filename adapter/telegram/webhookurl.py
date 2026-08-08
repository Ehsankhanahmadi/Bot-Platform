import httpx



response = httpx.get("http://127.0.0.1:4040/api/tunnels")
url = response.json()["tunnels"][0]["public_url"]
print(url)