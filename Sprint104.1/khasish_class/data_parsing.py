with open('student_details.txt', 'r') as file_obj:
    data = file_obj.read()
    student_data = data.split('\n\n')
    stu_result = []
    for student in student_data:
        lines = student.split('\n')
        print(lines)
        student_grade = {}
        student_grade['name'] = lines[0]
        student_grade['grade'] = [int(x) for x in lines[1:] if x.strip()]
        stu_result.append(student_grade)
#print(student)
#print(data)
print(stu_result)
