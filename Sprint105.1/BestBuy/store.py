import products as products

from products import Product

class Store:
    """
            Represents the store class that contains a list of products.
     """
    def __init__(self, products=[]):

        """
        Initializes a store instances with a list of products.

        Args:
            products (list, optional): List of Product instances. Defaults to an empty list.
        """
        self.products = products

    def add_product(self, new_product):
        """
        Adds a product to the store.

        Args:
           A product instances will be added into the list of store.
        """
        if new_product in self.products:
            self.products.append(new_product)
        else:
            raise ValueError("Product not found in the store.")


    def remove_product(self, rem_product):
        """
        Removes a product to the store.

        Args:
           A product instances will be removed from the list of store.

        """
        if rem_product in self.products:
            self.products.remove(rem_product)
        else:
            raise ValueError("Product not found in the store.")

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of the product from the store list
        Args:

        Returns:
            It returns how many items it the store in total.

        """
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity

    def get_all_products(self) -> list[Product]:
        """
         Returns a list of all active products in the store.

        Returns:
            List[Product]: List of active Product instance[]s.
        """
        # active_product = []
        # for item_product in self.products:
        #     if item_product.is_active():
        #         active_product.append(item_product)
        # return active_product
        active_products = [product for product in self.products if product.is_active()]
        return active_products


    def  order(self, shopping_list) -> float:
        """
        Buys the products from the shopping list and returns the total price of the order.

        Args:
            shopping_list (list): List of tuples, where each tuple contains a Product and a quantity.

        Returns:
            float: Total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                if product.quantity >= quantity:
                    total_price += product.buy(quantity)
                else:
                    raise ValueError(f"Insufficient quantity for {product.name}")
            else:
                raise ValueError(f"Product {product.name} is not available or not active")
        return total_price


if __name__ == "__main__":

    # product_list = [Product(name="MacBook Air M2", price=1450, quantity=100),
    #                 Product(name="Bose QuietComfort Earbuds", price=250, quantity=500),
    #                 Product(name="Google Pixel 7", price=500, quantity=250),
    #                 ]
    #
    # store = Store(product_list)
    # products = store.get_all_products()
    # print(store.get_total_quantity())
    # print(store.order([(products[0], 1), (products[1], 2)]))

    bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product(name="MacBook Air M2", price=1450, quantity=100)
    store = Store([bose, mac])
    price = store.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")




#     # Creating some Product instances
#     bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity=500)
#     mac = Product(name="MacBook Air M2", price=1450, quantity=100)
#
#     # Creating a Store instance with initial products
#     store = Store([bose, mac])
#
#     # Creating a new Product instance
#     pixel = Product("Google Pixel 7", price=500, quantity=250)
#
#     # Adding the new product to the store
#     store.add_product(pixel)
#
#     # Printing the products in the store before removal
#     for product in store.products:
#         print(product.name)
#
#     # Output:
#     # Bose QuietComfort Earbuds
#     # MacBook Air M2
#     # Google Pixel 7
#
#     # Removing a product from the store
#     store.remove_product(mac)
#
#     # Printing the products in the store after removal
#     for product in store.products:
#         print(product.name)
#
#     # Output:
#     # Bose QuietComfort Earbuds
#     # Google Pixel 7
#     print(store.get_total_quantity())
#     # Creating a Store instance with initial products
#     store = Product([bose, mac, pixel])
#     print((store.get_all_products()))
#     # Creating a shopping list
#     shopping_list = [(bose, 2), (pixel, 3)]
#     # Placing an order
#     total_order_price = store.order(shopping_list)
#
#     print(f"Total order price: ${total_order_price:.2f}")


