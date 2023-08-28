import  __main__
orderlist = []
while True:
    print("When you want to finish order, enter empty text.")
    product_num = int(input("Which product do you want from the list"))
    amount = int(input("What amount of product to want"))
    if not product_num:
        break
    orderlist.append(stroge_obj.get_all_products()[product_num][amount])
    print("Product added to the list")

total_payment = stroge_obj.order[orderlist]
print("--------")
print(f"Order has placed!! Total Amount: {total_payment}")