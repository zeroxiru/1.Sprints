with open ('student_details.txt', 'r')  as file_obj:
    data = file_obj.read()
    student_data = data.split('\n\n')
    result = []
    for student in student_data:
        each_line = student.split('\n')
        student_info = {}
        student_info['name'] = each_line[0]
        student_info['grade'] = [int(x) for x in each_line[1:] if x.strip()]
        result.append(student_info)
print(result)