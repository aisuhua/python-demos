import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(r.status_code)

json = r.json()
print(type(json))
print(json.keys())


