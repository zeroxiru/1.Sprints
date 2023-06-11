
SIMPLE_CLASSROOM_PATH = "classroom_simple.txt"


def parse_simple_classroom(file_path):
    """Parse classroom file that is given in `file_path` parameter.
    Returns a list of dictionaries describing the students in the classroom,
    each student is described with the dictionary: {
        'name': ...,
        'country': ...,
        'grades': [...]
    }"""
    students = []
    try:
        with open(SIMPLE_CLASSROOM_PATH, "r") as file_obj:
            lines_of_data = file_obj.readlines()
            number_of_lines_data = len(lines_of_data)
        index = 0

        while index + 1 < number_of_lines_data:
            line = lines_of_data[index].strip()

            if line and not line.startswith("###"):
                name = line
                country = lines_of_data[index + 1].strip()
                grades = []

                index += 2  # Increment index to move to the next line

                while index < number_of_lines_data and lines_of_data[index].strip() != "":
                    grade = lines_of_data[index].strip()
                    try:
                        grades.append(int(grade))
                    except ValueError:
                        print(f"Invalid grade: {grade}")
                    index += 1

                student = {
                    'name': name,
                    'country': country,
                    'grades': grades
                }

                students.append(student)

            index += 1
    except FileNotFoundError:
        print(f"File not found {file_path}")

    return students


def student_avg(students_list, student_name):
    for  student in students_list:
        if student["name"] == student_name:
            grades = student['grades']
            if grades:
                return sum(grades) / len(grades)
            else:
                return None
    return  None


def main():
    """Main function to interact with the user."""
    file_path = SIMPLE_CLASSROOM_PATH
    students = parse_simple_classroom(file_path)

    for student in students:
        print(student, "\n")

    try:
        student_name = input("Enter the name of the Student: ")
        average_grade = student_avg(students, student_name)
        if average_grade is not None:
            print(f"Average grade for {student_name}: {average_grade}")
        else:
            print(f"No data found for student name : {student_name} ")
    except KeyboardInterrupt:
        print('\n Program terminated by the user')


if __name__ == '__main__':
    main()
