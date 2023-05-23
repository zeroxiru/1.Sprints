import json


def load_data(file_path):
    with open(file_path, "r") as filehandle:
        return json.load(filehandle)


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">Name: {animal_obj["name"]}</div>\n'
    output += f'<div class="card__text">Diet: {animal_obj["characteristics"].get("diet", "Unknown")}</div>\n'
    output += f'<div class="card__text">Location: {animal_obj["locations"][0] if animal_obj["locations"] else "Unknown"}</div>\n'
    output += f'<div class="card__text">Type: {animal_obj["characteristics"].get("type", "Unknown")}</div>\n'
    output += '</li>\n'
    return output


def print_animal_details(animals_data):
    output = ''
    for animal in animals_data:
        serialized_animal = serialize_animal(animal)
        output += serialized_animal

    return output


def main():
    animals_data = load_data('animals_data.json')
    output = print_animal_details(animals_data)

    html_template = '''
    <html>
    <head>
        <style>
        @gray-darker:               #444444;
        @gray-dark:                 #696969;
        @gray:                      #999999;
        @gray-light:                #cccccc;
        @gray-lighter:              #ececec;
        @gray-lightest:             lighten(@gray-lighter,4%);


        html {
          background-color: #ffe9e9;
        }

        h1 {
            text-align: center;
            font-size: 40pt;
            font-weight: normal;
        }

        body {
          font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
          font-style: normal;
          font-weight: 400;
          letter-spacing: 0;
          padding: 1rem;
          text-rendering: optimizeLegibility;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
          -moz-font-feature-settings: "liga" on;
          width: 900px;
          margin: auto;
        }

        .cards {
          list-style: none;
          margin: 0;
          padding: 0;
        }

        .cards__item {
          background-color: white;
          border-radius: 0.25rem;
          box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
          overflow: hidden;
          padding: 1rem;
          margin: 50px;
        }

        .card__title {
          color: @gray-dark;
          font-size: 1.25rem;
          font-weight: 300;
          letter-spacing: 2px;
          text-transform: uppercase;
        }

        .card__text {
          flex: 1 1 auto;
          font-size: 0.95rem;
          line-height: 2;
          margin-bottom: 1.25rem;
        }
        ul.cards {
            list-style-type: none; /* Hide the list markers */
            padding: 0; /* Remove default padding */
        }
        </style>
    </head>
    <body>
        <h1>My Animal Repository</h1>
        <ul class="cards">
            {animals_info}
        </ul>
    </body>
    </html>
    '''
    html_output = html_template.format( "__REPLACE_ANIMALS_INFO__", output)

    # Write the HTML output to a file
    with open('animals.html', 'w') as file:
        file.write(html_output)

    print("animals.html file has been created.")


if __name__ == '__main__':
    main()
