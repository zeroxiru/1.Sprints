print("Welcome to the Python calculator!")
calculation = input("What do you want to calculate?\n")
if '+' in calculation and len(calculation.split("+")) == 2:
  first_number, second_number = calculation.split("+")
  if  len(first_number) == 1 and len(second_number) == 1 and first_number.isdigit() and second_number.isdigit():
      addition = int(first_number) + int(second_number)
      print("The answer is:", addition)
  else:
        print ("Invalid input: please enter the single digit numbers only.")
else:
    print("Invalid Input:Please enter a valid input with the calculation value of 1+2")


