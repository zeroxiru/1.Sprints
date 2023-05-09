import requests
import json

search_term = input("Enter the search term: ")

url = "https://www.readingrockets.org/bookfinder"  # Replace with the actual search API URL

params = {
    "query": search_term,
    "limit": 10,  # Adjust the limit as per your requirements
    "sort": "relevance"  # Adjust the sorting parameter as per your requirements
}

response = requests.get(url, params=params)

if response.status_code == 200:
    # Assuming the API response contains a JSON object with a 'results' key
    data = response.json()
    for result in data["results"]:
        download_url = result["download_url"]
        # Perform the download operation using 'download_url'
        # You can use a library like 'requests' to download the file
        # For example: requests.get(download_url).content
        print("Downloaded:", download_url)
else:
    print("Failed to retrieve search results. Status code:", response.status_code)
