n_students = int(input("Enter the number of students: "))
averages = []
for i in range(n_students):
    print(f"*** Student {i + 1}")
    list_of_grades = get_grades()
    averages.append(average_grade)

for i in range(n_students):
    print(f"Student {i} average: {averages[i]}")



def get_grades():
    list_of_grades = []
    grade = int(input("Enter a grade (-1 to stop): "))
    while grade != -1:
        list_of_grades.append(grade)
        grade = int(input("Enter a grade (-1 to stop): "))
    average_grade = sum(list_of_grades) / len(list_of_grades)


def calculate_avg():
    # def get_averages(students_dict):
    #
    #     averege_of_student = {}
    #     for student in students_dict:  # type(student) =str
    #         sum = 0
    #         # iterate through students and gets grades for matchin student in dictionary
    #         grades = students_dict[student]  # it is another dictionary depends how many entries you did
    #         for grade in grades:  # type(grade) = dict
    #             sum += grades[grade]
    #         averege_of_student[student] = sum / len(grades)
    #     return averege_of_student
    #
    # # ***** Test for get_averages(students_dict)
    # # students_grades = {'STUDENT0': {'GRADE1': 10, 'GRADE2': 20},
    # #                    'STUDENT1': {'GRADE1': 20, 'GRADE2': 30}}
    #
    # def print_averages(dict_of_last):
    #     for key, val in dict_of_last:
    #         print(f'{key}:{val}')
    #
    # def main():
    #
    #     students_grades = get_grades()
    #     avegerage_of_student = get_averages(students_grades)
    #     print(avegerage_of_student)
    #
    # if __name__ == '__main__':
    #     while True:
    #         main()
    #         ask = input('Do you wanto to keep testing y/n ')
    #         if 'y' not in ask.lower():
    #             break  # you do not need to add else statement