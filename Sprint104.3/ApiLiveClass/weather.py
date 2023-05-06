import requests

url = "https://open-weather13.p.rapidapi.com/city/dhaka"

headers = {
	"X-RapidAPI-Key": "6c29366492mshd454e15806fb482p101beejsnd34153fa8684",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

query_params = {
    "city": "uk",
    #"city": "bd"

}

response = requests.get(url, headers=headers, params=query_params)

print(response.json())