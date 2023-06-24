with open("grades-original.csv", "r") as file_obj_r:
    data = file_obj_r.readlines()
with open("grades-bonus.csv", "w") as file_obj_w:
    for i, line in enumerate(data):
        line = line.strip()
        if i == 0:
            file_obj_w.write(f"{line}\n")
        else:
            elements = line.split(",")
            if len(elements) == 3:
                name = elements[0]
                score = elements[1]
                grade = elements[2]
                new_score = int(score) + 10
                file_obj_w.write(f"{name},{new_score},{grade}\n")
            else:
                file_obj_w.write(f"{line}\n")