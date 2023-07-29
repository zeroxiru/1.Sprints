import requests
#
# name = 'majenda fox'
# api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
# response = requests.get(api_url, headers={'X-Api-Key': 'q8961PVDHmB2hxiC0G4dOQ==UAQBZam6HY1bGvw1'})
# if response.status_code == requests.codes.ok:
#     print(response.json())
# else:
#     print("Error:", response.status_code, response.json())import requests

name = 'foxnhe'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'q8961PVDHmB2hxiC0G4dOQ==UAQBZam6HY1bGvw1'})
if response.status_code == requests.codes.ok:
    print(response.json())
elif response.status_code == 404:
    print("Animal not found.")
else:
    print("Error:", response.status_code, response.json())

