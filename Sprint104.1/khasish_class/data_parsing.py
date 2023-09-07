# with open('student_details.txt', 'r') as file_obj:
#     data = file_obj.read()
#     student_data = data.split('\n\n')
#     stu_result = []
#     for student in student_data:
#         lines = student.split('\n')
#         print(lines)
#         student_grade = {}
#         student_grade['name'] = lines[0]
#         student_grade['grade'] = [int(x) for x in lines[1:] if x.strip()]
#         stu_result.append(student_grade)
# #print(student)
# #print(data)
# print(stu_result)

result = []

def get_user_object(file_handle):
    user_info = {}
    # read id
    line = file_handle.readline()
    if len(line) == 0:  # EOF signal
        return
    user_info['id'] = line[1:].strip()

    # read name
    line = file_handle.readline()
    user_info['name'] = line.split(":")[1].strip()

    # read age
    line = file_handle.readline()
    user_info['age'] = int(line.split(":")[1].strip())

    # read favorite foods
    user_info['favorite_foods'] = []
    line = file_handle.readline()  # Skip the "Favorite_Foods:" line
    while True:
        line = file_handle.readline().strip()
        if not line:
            break
        user_info['favorite_foods'].append(line)

    # read purchase_history
    user_info['purchase_history'] = []
    line = file_handle.readline()  # Skip the "Purchase_History:" line
    while True:
        line = file_handle.readline().strip()
        if not line:
            break
        try:
            purchase = int(line)
            user_info['purchase_history'].append(purchase)
        except ValueError:
            # Skip lines that can't be converted to integers
            continue

    return user_info

with open("user_info1.txt", 'r') as file_handler:
    while True:
        returned_object = get_user_object(file_handler)
        if returned_object is None:
            break
        result.append(returned_object)

print(result)
