import json


def load_data(file_path):

    with open(file_path, "r") as filehandle:
        return json.load(filehandle)

def get_animals_data(data):
    animals_data = {}
    animals_data["Name"] = data["name"]
    animals_data["Diet"] = data["characteristics"]["diet"]
    animals_data["Locations"] = data["locations"]
    animals_data["Type"] = data["characteristics"]["type"]
    return animals_data

output = ''  # define an empty string
for animal_data in data:
    # append information to each string
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"

print(output)

def main():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        print(get_animals_data(animal))

if __name__ == '__main__':
    main()
#
# animals_data = load_data('animals_data.json')
# formatted_data = json.dumps(animals_data, indent=4)

# for animals in animals_data:
#         name = animals.get("Name")
#         diet = animals.get("Diet")
#         locations = animals.get("Locations")
#         animal_type = animals.get("Type")
#
# if name and diet and locations and animal_type:
#         location = locations[0] if locations else None
#         print("Name:", name)
#         print("Diet:", diet)
#         if location:
#             print("Location:", location)
#         print("Type", animal_type)




