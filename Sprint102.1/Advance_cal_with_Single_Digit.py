
print("Welcome to the Python calculator!")
number_of_calculation = int(input("How many calculations do you want to do?\n"))
for i in range(number_of_calculation):
  calculation = input("What do you want to calculate?\n")
  if '+' in calculation:
    first_number, second_number = calculation.split("+")

    if len(first_number) == 1 and len(second_number) == 1 and first_number.isdigit() and second_number.isdigit():
        addition = int(first_number) + int(second_number)
        print("The answer is:", addition)
    else:
        print("Invalid input: please enter the single digit numbers only.")
  elif '-' in calculation:
    first_number, second_number = calculation.split("-")
    if len(first_number) == 1 and len(second_number) == 1 and first_number.isdigit() and second_number.isdigit():
        subtraction = int(first_number) - int(second_number)
        print("The answer is:", subtraction)
    else:
        print("Invalid input: please enter the single digit numbers only.")

  elif '*' in calculation:
    first_number, second_number = calculation.split("*")
    if len(first_number) == 1 and len(second_number) == 1 and first_number.isdigit() and second_number.isdigit():
        multiplication = int(first_number) * int(second_number)
        print("The answer is:", multiplication)
    else:
        print("Invalid input: please enter the single digit numbers only.")
  elif '/' in calculation:
    first_number, second_number = calculation.split("/")
    if len(first_number) == 1 and len(second_number) == 1 and first_number.isdigit() and second_number.isdigit():
        division = int(first_number) / int(second_number)
        print("This answer is:", division)
  elif '~' in calculation:
    first_number, second_number = calculation.split("~")
    if len(first_number) == 1 and len(second_number) == 1 and first_number.isdigit() and second_number.isdigit():
        quotient = int (first_number)// int (second_number)
        remainder = int(first_number) % int(second_number)
        print("This answer is:", quotient)
        print("This remainder is:", remainder)
  else:
    print("Invalid Input:Please enter a valid input with the calculation value of 1+2")


