import json

import requests

API_KEY = "6d44d8f3-462d-465f-9280-08cb60b98114"
year = "2022"
country = "BD"
API_URL = f"https://holidayapi.com/v1/holidays?pretty&key={API_KEY}&country={country}&year={year}"


def make_api_requests(country):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        countrywise_holiday = json_response["holidays"]
        for holiday in countrywise_holiday:
            country_holiday_name = holiday["name"]
            print(country_holiday_name)
        #print(countrywise_holiday["name"])

    elif response.status_code == 403:
        print("Access to the API is forbidden. Please check your API key and permissions.")
    else:
        print("Request failed with status code:", response.status_code)

def list_of_countries():
    response_list_of_countries = requests.get(f"https://holidayapi.com/v1/countries?pretty&key={API_KEY}")
    countries_list = response_list_of_countries.json()
    countries = countries_list["countries"]
    for country in countries:
        country_name = country["name"]
        print( country_name)

#def list




def main():
    print("Available country name are as below: ")
    list_of_countries()
    user_specific_country = input("Enter the name of the Country: ")
    print(f"List of holidays in the year of {year}")
    make_api_requests(user_specific_country)

if __name__ == "__main__":
    main()
