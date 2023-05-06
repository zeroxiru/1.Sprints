def get_prices_and_discount_amount_from_user():

    input_line = input("Enter the prices: ")
    list_of_prices_str = input_line.split(",")
    list_of_prices_int = []
    for price in list_of_prices_str:
        list_of_prices_int.append(int(price))
    discount_percent = int(input("Enter the discount percentage amount: "))



    return list_of_prices_int, discount_percent

def apply_discount_on_single_price(price, discount_percent):
    return (price * (1-discount_percent/100))

def apply_discount_on_list_of_prices(price_list, discount_percent):
    list_of_discount_prices = []
    for price in price_list:
        list_of_discount_prices.append(apply_discount_on_single_price(price,discount_percent))
    return list_of_discount_prices

def main():
    list_of_prices, discount_percent = get_prices_and_discount_amount_from_user()
    list_of_discounted_prices = apply_discount_on_list_of_prices(list_of_prices, discount_percent)
    print(list_of_discounted_prices)


if __name__ == "__main__":
    main()




#print(get_prices_and_discount_amount_from_user())
#print(apply_discount_on_single_price(1000,30))

#print(apply_discount_on_list_of_prices([50,100,500,1000],15))

