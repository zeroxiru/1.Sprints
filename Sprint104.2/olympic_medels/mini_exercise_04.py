with open("olympic-medals.csv", "r") as file_obj_r:
    data = file_obj_r.readlines()

with open("olympic-medals-5.csv", "w") as file_obj_w:
    for i, line in enumerate(data):
        line = line.strip()
        if i == 0:
            file_obj_w.write(f"{line}\n")
        else:
            elements = line.split(",")
            if len(elements) == 4:
                team = elements[0]
                gold = int(elements[1])
                silver = int(elements[2])
                bronze = int(elements[3])
                if gold >= 5:
                     file_obj_w.write(f"{team},{gold},{silver},{bronze}\n")
                    #file_obj_w.write(f"{line}\n")

