import requests
import json

url = "https://reqres.in/api/users"
#url = "http://www.absolutelynothing.com"
#url = "http://www.absolutelynothing.com/something"
#url = "http://doesthisevenexist.com"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for user in data["data"]:

        print(user["url"])
else:
    print("status code", response.status_code)