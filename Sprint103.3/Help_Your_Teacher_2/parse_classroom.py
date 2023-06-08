import json

SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"


def parse_simple_classroom(file_path):
  """ Parse classroom file that is given in `file_path` parameter.
  Returns a list of dictionaries describing the students in the classroom,
  each student is describe with the dictionary: {
    'name': ...,
    'country': ...,
    'grades': [...]
  }"""
  with open("", r) as file_obj:



print(parse_simple_classroom(SIMPLE_CLASSROOM_PATH))
