import json

import requests
import json

def main():
    res = requests.get("https://fruityvice.com/api/fruit/all")
    #print(type(res.text))
    fruits_info = json.loads(res.text)
    sorted_fruits_info = sorted(fruits_info, key=lambda x: x["id"] )
    #print(type(parsed))
    for fruit in sorted_fruits_info:
        print(fruit["name"], fruit["id"])

if __name__ == "__main__":
    main()