import httpx



response = httpx.get("http://127.0.0.1:4040/api/tunnels")
url = response.json()["tunnels"][0]["public_url"]
print(url)

response = httpx.get("http://127.0.0.1:4041/api/tunnels")
url = response.json()["tunnels"][0]["public_url"]
print(url)

response = httpx.get("http://127.0.0.1:4042/api/tunnels")
url = response.json()["tunnels"][0]["public_url"]
print(url)