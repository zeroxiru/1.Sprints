import sys


def add_a_contact():
    name = input("Enter the name of the contact:")
    c_number = input(f"Enter the phone number of {name}:")

    # validating the phone number.
    if validate_number(c_number):
        # Adding the phone number to the phone book dictionary.
        phone_book[name] = c_number
        print(f"Contact Added: {name}: {c_number}")
    else:
        print("Invalid contact number. Contact number  is not added.")

    if phone_book != {}:
        i = 1
        for key, value in phone_book.items():
            print(f"{i}. {key}: {value} ")
            i += 1
    else:
        print("The contact number is not available in the phone book.")

def remove_contact():
    phone_name =input("Enter the contact name to delete from the phone book contact.")
    if phone_name in phone_book:
        print(f"{phone_name} = {phone_book[phone_name]}")
    else:
        print(f'{phone_name} was not found in the phone book contact')
        ask = input("Do you want to delete the contact Y/N")
        if "Y" in ask.upper():
            del phone_book[phone_name]

def search_contact(phone_book):
    contact_name = input("Enter the contact name to search from the phone book contact:")
    name_lower = contact_name.lower()

    # iterate over the phone book to search the contact name
    found = False
    for contact_name, contact_number in phone_book.items():
        if contact_name.lower() == name_lower:
            print(f"The contact number for {contact_name} is: {contact_number}")
            found = True
    if not found:
        print(f"No contact found for the name: {contact_name}")



def validate_number(number):
    # check the length of the number.
    if not 6 <= len(number) <= 13:
        return False
    # check all the allowed characters are available in the number.
    allowed_characters = set("0123456789-+")
    if not all(char in allowed_characters for char in number):
        return False
    # checking the placement of "-" and "+" sign
    if number.count("-") != 1 and number.count("+") > 1 or (number.count("+") == 1 and number[0] != "+"):
        return False
    # checking if there are digits between the hyphen and plus sign (if present)
    if '_' in number and not number.split("-")[1].isdigit():
        return False
    return True



# main menu
def main():
  menu = """ 
**********Welcome to the phone book app!**************
Menu:
Select an action:
1. Add a contact
2. Remove a contact
3. Search for a contact
4. View the phone book
5. Exit
Enter your choices from(1 to 5) for perform your task:
\n """
  while True:
      command = int(input(f"{menu} choose between 1 to 5:"))
      if 0 < command < 6:
          if command == 1:
              add_a_contact()
          elif command == 2:
               remove_contact()
          elif command == 3:
               search_contact(phone_book)
          # elif command == 4:
          #     view_the_contact()
          elif command == 5:
              print("Goodbye!")
              break
      else:
          print(" Invalid choice. Please try again.")





# print(validate_number("123224343234248"))
# print(validate_number("+01752-33-2312"))

if __name__ == "__main__":
    phone_book = {
    "Jane": "+234-567890",
    "Alice": "+345-6789012",
    "Bob": "+456-7890123",
    "Charlie": "+56890-12345",
    "David": "+67890-123456",
    "Eve": "+7890123-4567",
    "Frank": "+890-12345678",
    "Grace": "+901-23456789",
    "Henry": "+012-34567890",
    "Isabella": "+123-45689012",
    "Jack": "+234-56789012",
    "Kate": "+345-678901234",
    "Liam": "+456-789012345",
    "Mia": "+56789-0123456",
    "John": "+123-456989",
}
    main()