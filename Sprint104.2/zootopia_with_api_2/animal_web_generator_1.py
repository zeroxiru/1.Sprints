import data_fetcher


def get_animal_step1_data(data):
    """
        Extracts and prints the step 1 information for each animal.

        Args:
            data (list): The list of animal data as dictionaries.

        Prints:
            prints the animal_data
        """

    # animal_data = {}
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
    return output


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


def serialize_animal(animal_obj):
    def serialize_animal(animal_obj):
        """
        Serializes an animal object into a formatted string representation.

        Parameters:
            animal_obj (object): An instance of the Animal class or its subclasses.

        Returns:
            str: A string representing the serialized animal object.

        Raises:
            TypeError: If animal_obj is not an instance of the Animal class or its subclasses.

        Description:
            This method takes an animal object and converts it into a formatted string representation.
            The animal object must be an instance of the Animal class or its subclasses. The method
            serializes the object by extracting its properties and formatting them into a string.


        """

    output_serl = ''
    output_serl += '<li class="cards__item">\n'
    output_serl += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output_serl += '<p class="card__text">\n'
    output_serl += '<ul>\n'

    if animal_obj.get("locations"):
        output_serl += f'<li> <span style="font-weight: bold;">Location:</span> ' \
                  f'{animal_obj["locations"][0]}</li>\n'

    if animal_obj["taxonomy"].get("scientific_name"):
        output_serl += f'<li> <span style="font-weight: bold;">Scientific ' \
                  f'Name:</span> {animal_obj["taxonomy"]["scientific_name"]}</li>\n'

    if animal_obj["characteristics"].get("type"):
        output_serl += f'<li> <span style="font-weight: bold;">Type:</span> ' \
                  f'{animal_obj["characteristics"]["type"]}</li>\n'

    if animal_obj["characteristics"].get("diet"):
        output_serl += f'<li> <span style="font-weight: bold;">Diet:</span> ' \
                  f'{animal_obj["characteristics"]["diet"]}</li>\n'

    output_serl += '</ul>\n'
    output_serl += '</p>\n'
    output_serl += '</li>\n'

    return output_serl


def print_with_serialization(animals_data):

    """
    Serializes a list of animal objects and returns a formatted string representation.

    Parameters:
        animals_data (list): A list of animal objects to be serialized.

    Returns:
        str: A string representing the serialized animal objects.

    Description:
        This method takes a list of animal objects and serializes each object into a formatted string representation.
        The animal objects must be instances of the Animal class or its subclasses. The method iterates over the
        animals_data list, calling the 'serialize_animal' function to serialize each animal object.

        The serialized string for each animal object is appended to the 'output_serl' variable, which holds the
        cumulative serialized representation of all animal objects. The final 'output_serl' string is returned.

        The serialization process includes extracting the properties of each animal object, such as name, species,
        age, and any additional attributes specific to the animal subclass. The string representation is formatted
        in a human-readable way, allowing for easy storage, transmission, or display of the serialized data.

        If any object in the animals_data list is not a valid animal object, an exception may be raised by the
        'serialize_animal' function. It's important to ensure that only valid animal objects are included in the
        animals_data list to avoid potential errors during serialization.
    """

    output_serl = ''
    for animal in animals_data:
        serialized_animal = serialize_animal(animal)
        output_serl += serialized_animal

    return output_serl



def main():
    search_name = input("Enter the animal name for search: ")
    data = data_fetcher.fetch_data(search_name)
    if data:

        print(data)
    # Generate HTML file for get_animal_step1_data
        output_step1 = get_animal_step1_data(data)
    # print(output_step1)
        html_template_step1 = reading_html_template_file("animals_template.html")
        html_output_step1 = html_template_step1.replace('__REPLACE_ANIMALS_INFO__', output_step1)
        with open('animals.html', 'w') as fileobj_step1:
            fileobj_step1.write(html_output_step1)
        print("animals.html file has been created.")

    # # Generate HTML file for print_with_serialization
        output_serialization = print_with_serialization(data)
        html_template_serialization = reading_html_template_file("animals_template.html")
        html_output_serialization = html_template_serialization.replace('__REPLACE_ANIMALS_INFO__', output_serialization)
        with open('animals_serialization.html', 'w') as fileobj_serialization:
            fileobj_serialization.write(html_output_serialization)
        print("animals_serialization.html file has been created.")
    else:

        # Error message for  non-existent animal
        # print("Animal data not found or error occurred.")
        error_message = f'<h2>The animal "{search_name}" doesn\'t exist.</h2>'
        html_error_message = reading_html_template_file('animals_template.html')
        html_output_error = html_error_message.replace('__REPLACE_ANIMALS_INFO__', error_message)
        with open('animals_error.html', 'w') as fileobj_error:
            fileobj_error.write(html_output_error)
        print("animals_error.html file has been created.")





if __name__ =="__main__":
    main()