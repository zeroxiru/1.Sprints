def shopping_cart_func():
    # creating an empty shopping cart  dictionary
    shopping_cart = {}
    while True:
     item = input("Enter the Item to insert(done to exit): ")
     if item == 'done':
      break
     elif item == "add":
           key = input("Enter the name of the Item to add")
           if key in shopping_cart:
                quantity = int(input("Enter quantity to add:"))
                shopping_cart[key] += quantity
           else:
             print("Item not found in the shopping cart")
     elif item == "show":
         for item, quantity in shopping_cart.items():
             print(item, quantity)
         break
     else:
        quantity = int (input("Enter the Quantity of the Item:"))
        shopping_cart[item] = quantity
    return shopping_cart

shopping_cart_func()