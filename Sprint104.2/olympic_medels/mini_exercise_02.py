with open("olympic-medals.csv", "r") as file_obj_r:
    data = file_obj_r.readlines()[:10]

with open("olympic-medals-short.csv", "w") as file_obj_w:
    for line in data:
        file_obj_w.write(line)
