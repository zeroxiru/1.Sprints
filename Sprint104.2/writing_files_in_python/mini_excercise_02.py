user_input = int(input("Enter a valid integer number: "))

with open("nums.txt", "w") as fileobj_w:
    for number in range(1, user_input+1):
        fileobj_w.write(f"{number}\n")