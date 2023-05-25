total_number = 0
while True:
    user_input = input("Enter a number (or 'n' to quit the program): ")
    if user_input == 'n':
        break

    try:
        value = int(user_input)
        total_number += value
    except ValueError:
        print("Invalid input")

print("Total:", total_number)