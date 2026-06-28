import requests
r=requests.get("https://yandex.ru")
print(r.status_code)
cl