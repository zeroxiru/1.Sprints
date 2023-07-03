import json

with open("holiday_eddited.json", "r", encoding="utf-8") as file_obj:
    data = file_obj.read()
    data = json.loads(data)
    countries = data["countries"]
    for country in countries:
        country_name = country["name"]
        print(country_name)

