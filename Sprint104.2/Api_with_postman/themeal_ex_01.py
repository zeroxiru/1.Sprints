import requests
import json



def search_meal(meal_name):
    meal_data = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}")
    response = meal_data.json()
    print(response)

def main():
    while True:
        user_meal_desc = input("Enter the name of the meal: ")
        search_meal(user_meal_desc)
        if user_meal_desc == "exit":
            exit()

if __name__ == "__main__":
    main()

