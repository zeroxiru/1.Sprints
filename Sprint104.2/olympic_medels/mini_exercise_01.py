with open("olympic-medals.csv", "r") as file_obj_r:
    data = file_obj_r.read()

with open("olympic-medals-copy.csv", "w") as file_obj_w:
    file_obj_w.write(data)
