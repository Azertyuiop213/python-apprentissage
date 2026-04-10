import requests

# response = requests.get("https://httpbin.org/get")
# data = response.json()
# print(response.status_code)
# print(data["url"])
try:
    site = input("Enter a website URL: ")
    response = requests.get(site)
    if response.status_code == 200:
        print("le site est en ligne")
    else:
        print(f"Code : {response.status_code}")
except requests.exceptions.ConnectionError:
    print("site introuvable")