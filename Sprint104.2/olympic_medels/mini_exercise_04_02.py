with open("olympic-medals.csv", "r") as file_obj_r:
    data = file_obj_r.readlines()

with open("olympic-medals-5.csv", "w") as file_obj_w:
    header = data[0]  # Extract the header line
    file_obj_w.write(header)  # Write the header line to the new file

    for line in data[1:]:  # Skip the header line and iterate over the remaining lines
        line = line.strip()
        elements = line.split(",")
        if len(elements) == 4:
            team = elements[0]
            gold = int(elements[1])
            silver = int(elements[2])
            bronze = int(elements[3])
            if gold >= 5:
                file_obj_w.write(f"{line}\n")
