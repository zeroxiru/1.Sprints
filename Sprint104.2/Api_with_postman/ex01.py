import requests
import json
def main():
    response = requests.get("https://fruityvice.com/api/fruit/all")
    fruits_info = json.loads(response.text)
    for fruits in fruits_info:
        print(fruits)

if __name__ == "__main__":
    main()
