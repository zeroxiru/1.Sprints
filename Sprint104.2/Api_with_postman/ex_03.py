import json
import requests


def get_fruit_nutritions(fruit_name):
    fruit_data = requests.get(f"https://fruityvice.com/api/fruit/{fruit_name}")
    response = fruit_data.json()
    return response["nutritions"]


def main():
    all_fruit_data = requests.get("https://fruityvice.com/api/fruit/all")
    response = all_fruit_data.json()
    for fruit in response:
        print(fruit["name"])
        nutritions = get_fruit_nutritions(fruit["name"])
        print(nutritions)


if __name__ == "__main__":
    main()




