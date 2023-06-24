with open("olympic-medals.csv", "r") as file_obj_r:
    data = file_obj_r.readlines()

with open("olympic-medals-n.csv", "w") as file_obj_w:
    for i, line in enumerate(data):
        line = line.strip()
        if i == 0 or line.startswith("N"):
            file_obj_w.write(f"{line}\n")
