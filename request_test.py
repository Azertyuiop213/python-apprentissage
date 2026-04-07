import requests

response = requests.get("https://httpbin.org/get")
data = response.json()
print(response.status_code)
print(data["url"])
