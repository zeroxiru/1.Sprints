import json

def load_data(file_path):
    """
    Loads the JSON animal data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: The loaded JSON data as a list of dictionaries.
    """
    with open(file_path, 'r') as file_obj:
        return json.load(file_obj)

def get_animal_step1_data(data):
    """
        Extracts and prints the step 1 information for each animal.

        Args:
            data (list): The list of animal data as dictionaries.

        Prints:
            prints the animal_data
        """
    animal_data = {}
    # for animal in data:
    #     animal_data["Name"] = animal["name"]
    #     animal_data["Diet"] = animal["characteristics"].get("diet", "Unknown")
    #     animal_data["Locations"] = animal.get("locations", [])
    #     animal_data["Type"] = animal["characteristics"].get("type", "Unknown")
    #     print(f'{animal_data}\n')


      # define a empty string.
    output = ""
    for animal in data:
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics'].get('diet', 'Unknown')}\n"
        output += f"Locations: {animal.get('locations', [])}\n"
        output += f"Type: {animal['characteristics'].get('type', 'Unknown')}\n"
    print(output)
def reading_html_template_file(html_template_file):

    """
    reading the animals_template.html file

    Args:
    animals_template.html file to read the html file

    returns:
    returns the content of the template file

    """
    with open(html_template_file, "r") as file_obj_r:
        template_content = file_obj_r.read()

    return template_content




def main():

    """
     The main entry point of the program.

     Loads the animal data, calls the 'get_animal_step1_data' method,
     and prints the step 1 information for each animal.

     Args:
         None

     Returns:
         None
     """
    animal_data = load_data("animals_data.json")
    #print(animal_data)
    get_animal_step1_data(animal_data)
    html_template = reading_html_template_file("animals_template.html")
    print(html_template)



if __name__ == "__main__":
    main()

