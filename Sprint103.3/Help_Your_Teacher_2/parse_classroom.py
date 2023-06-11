
SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"


def parse_simple_classroom(file_path):
    """ Parse classroom file that is given in `file_path` parameter.
     Returns a list of dictionaries describing the students in the classroom,
     each student is describe with the dictionary: {
       'name': ...,
       'country': ...,
       'grades': [...]
     }"""
    students = []
    with open(SIMPLE_CLASSROOM_PATH, "r") as file_obj:
        data = file_obj.read().strip().split("\n\n")
    for line in data:
        entry_lines = line.strip().split("\n")

        if len(entry_lines) >= 3 and entry_lines[0] == "###":
            name = entry_lines[1].strip()
            country = entry_lines[2].strip()
            grades = [int(grade.strip()) for grade in entry_lines[3:]]
            student = {
                "name": name.strip(),
                "country": country.strip(),
                "grades": grades
             }
            students.append(student)
    return students


print(parse_simple_classroom(SIMPLE_CLASSROOM_PATH))
