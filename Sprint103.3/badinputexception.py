bad_input = True
while bad_input:
    try:
        number = int(input("Enter a number: "))
        bad_input = False
    except ValueError as e:
        print("You entered something that is not a number! Error: ", e)

print("Thanks")
print(f"print the number {number}")
