def get_number_from_user():
    while True:
        try:
            number = int(input("Enter a number: "))
            print("Thanks!!")
            return number
        except ValueError as e:
            print(f"You entered something that is not a number! Error: , {e}")
number = get_number_from_user()
print(f'{number}')