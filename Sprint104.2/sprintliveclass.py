text = """Jonathan: 0542369112
Ron: 0542889423
Sharon: 039912315
Charles: 0548743210"""

for line in text.split("\n"):
    phone_num = line.strip().split(": ")[1]
    print(phone_num)

for line in text.split("\n"):
    phone_num = line.strip().split(":")[1]
    print(phone_num)

#
