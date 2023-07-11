import json
import requests


def get_fruit_nutritions(fruit_name):
    fruit_data = requests.get(f"https://fruityvice.com/api/fruit/{fruit_name}")
    response = fruit_data.json()
    return response["nutritions"]


def main():
    all_fruit_data = requests.get("https://api-ninjas.com/api/animals")
    response = all_fruit_data.json()
    for fruit in response:
        print(fruit["name"])
        characteristics = get_fruit_nutritions(fruit["prey"])
        print(characteristics)


if __name__ == "__main__":
    main()




