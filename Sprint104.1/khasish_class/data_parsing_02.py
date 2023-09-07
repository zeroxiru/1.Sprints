# with open ('student_details.txt', 'r')  as file_obj:
#     data = file_obj.read()
#     student_data = data.split('\n\n')
#     result = []
#     for student in student_data:
#         each_line = student.split('\n')
#         student_info = {}
#         student_info['name'] = each_line[0]
#         student_info['grade'] = [int(x) for x in each_line[1:] if x.strip()]
#         result.append(student_info)
# print(result)
#
# result = []
# student_grade = {}
# with open('student_details.txt', 'r') as file_obj:
#     for line in file_obj:
#         student_grade['name'] = line.strip()
#         grades = []
#         for grade in range(3):
#             grades.append(file_obj.readline().strip())
#         student_grade['grade'] = [int(x) for x in grades]
#         file_obj.readline()
#     result.append(student_grade)
#
# print(result)
#




result = []

with open('student_details.txt', 'r') as file_obj:
    for line in file_obj:
        students_grade_info = {}
        students_grade_info['name'] = line.strip()
        student_grades = []
        for grade in range(3):
            student_grades.append(file_obj.readline().strip())
        students_grade_info['grades'] = [int(x) for x in student_grades if x.strip()]
        file_obj.readline()
        result.append(students_grade_info)
print(result)


