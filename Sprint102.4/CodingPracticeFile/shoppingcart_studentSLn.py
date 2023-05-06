def add_item():
    item = input("Add item to list: ")
    quantity = int(input('How many do you want to add: '))
    if not item in basket:
        basket[item] = quantity
    else:
        basket[item] += quantity


def search_item():
    item = input('Enter the Item name: ')
    if item in basket:
        print(f'{item} = {basket[item]}')
    else:
        print(f'{item} was not found in basket')


def display_all():
    if basket != {}:
        for key, val in basket.items():
            print(f'{key}: {val}')
    else:
        print('Basket is empty')


def delete_item():
    item = input('Enter the Item name: ')
    if item in basket:
        print(f'{item} = {basket[item]}')
    else:
        print(f'{item} was not found in basket')
    ask = input('Do you want to delete it y/n? ')
    if 'y' in ask.lower():
        del basket[item]


def main():
    menu = '''
1. Add Item:
2. Seach Item In Basket
3. Display All
4. Delete Item
5. EXIT
Enter your command:\ '''

    while True:
        command = int(input(f'{menu}Choose Between 1 to 5: '))
        if 0 < command < 6:
            if command == 1:
                add_item()
            elif command == 2:
                search_item()
            elif command == 3:
                display_all()
            elif command == 4:
                delete_item()
            elif command == 5:
                break
        else:
            print('Chose Between 1 to 5')
            continue


if __name__ == '__main__':
    basket = {}
    main()