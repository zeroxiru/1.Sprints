import requests
import json


def main():
    response = requests.get("https://sallysbakingaddiction.com/#search/q=banana%20cake")
    cake_info = response.json()


if __name__ == "__main__":

    main()