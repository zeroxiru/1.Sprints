import requests


def fetch_data(animal_name):
    """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """

    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    headers = {'X-Api-Key': 'q8961PVDHmB2hxiC0G4dOQ==UAQBZam6HY1bGvw1'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == requests.codes.ok:
        return response.json()
    elif response.status_code == 404:
        print("Animal not found.")
        return None
    else:
        print("Error:", response.status_code, response.json())
        return None
