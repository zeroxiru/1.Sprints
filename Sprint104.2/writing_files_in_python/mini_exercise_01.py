
user_input = input("Write your name in the text file: ")
with open(f"{user_input}.txt", "w") as fileobj:


    fileobj.write(f"heloo {user_input}!")