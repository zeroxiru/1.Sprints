import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(store_obj):
    while True:
        print("Welcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please select an option: ")

        if choice == "1":
            store_obj.list_products()
        elif choice == "2":
            store_obj.show_total_amount()
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Thank you for using Best Buy. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def make_order(store_obj):
    product_name = input("Enter the product name you want to order: ")
    quantity = int(input("Enter the quantity you want to order: "))
    success = store_obj.make_order(product_name, quantity)
    if success:
        print("Order placed successfully!")
    else:
        print("Failed to place order. Please check product availability and quantity.")


if __name__ == "__main__":
    start(best_buy)
