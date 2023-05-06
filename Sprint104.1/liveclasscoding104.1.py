users = []

with open("user_info1.txt", "r") as file:
    data = file.read()
    user = {}
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if user:
                users.append(user)
            user = {"id": int(line[1:]), "favorite_foods": []}
        elif line.startswith("Name:"):
            user["name"] = line[6:].strip()
        elif line.startswith("Age:"):
            user["age"] = int(line[5:])
        elif line.strip():
            user["favorite_foods"].append(line.strip())

# Add the last user to the list
if user:
    users.append(user)

print(users)