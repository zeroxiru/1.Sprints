#https://software-engineering.masterschool.com/production-pages/apis-classwork
import requests

url = "https://streaming-availability.p.rapidapi.com/v2/services"

headers = {
	"X-RapidAPI-Key": "6c29366492mshd454e15806fb482p101beejsnd34153fa8684",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

# Set up the parameters for the API query
query_params = {
    "country": "us",
    "service": "netflix",
    "type": "movie",
    "genre": "comedy",
    "page": "1",
    "language": "en"
}

response = requests.get(url, headers=headers, params=query_params)

print(response.json())
#print(response.json.dumps(response.json(), indent=4))