result =[]
def get_user_object_by_readline(file_obj):

    user_info = {}
    # read line $ID
    line = file_obj.readline()
    if len(line) == 0:
        return
    user_info['id'] = line[1:].strip()
    # read $ name
    line = file_obj.readline()
    user_info['name'] = line.split(":")[1].strip()
    # read $Age
    line = file_obj.readline()
    user_info['age'] = int(line.split(":")[1].strip())
    print(user_info)
    # read Favorite foods
    line = file_obj.readline()
    favorite_food = []
    for line in file_obj:
        if line.startswith("\t"):
            favorite_food.append(line.strip())
        else:
            break

    user_info['Favorite_Foods'] = favorite_food
    print(user_info)

    purchase_history = []
    for line in file_obj.readline():
        if line.startswith("\t"):
            purchase_history.append(int(line.split().strip()))
        else:
            break
    user_info['purchase_history'] = purchase_history
    print(user_info)
    return user_info



with open ('user_info1.txt', 'r') as file_obj:
    while True:
        obj = get_user_object_by_readline(file_obj)
        if obj is None:
            break
        result.append(obj)
    print(result)




