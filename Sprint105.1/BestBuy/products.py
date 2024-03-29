
class Product:
    def __init__(self, name: str, price: float, quantity=int):
        """
        the constructor method initializes the product instances.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError Exceptions for  each  attributes of price, name, quantity.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        if price <= 0:
            raise ValueError("Name cannot be negative")
        if quantity < 0:
            raise ValueError("Name cannot be negative")
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_quantity(self) -> float:
        """
        Getter function for the quantity.

        Returns:
             float: The quantity of the product as a float.
        """

        return float(self._quantity)


    def set_quantity(self, quantity: int):
        """
        Set the initial value for the quantity. If the
        quantity value reaches 0 then deactivate the product true.
        Args:
            quantity (int): The new quantity of the product.

        """
        self._quantity = quantity
        if quantity == 0:
            self._active = False

    def is_active(self) -> bool:
        """
        Getter function for isActive.

        Returns:
            Returns True if the product is active (quantity > 0), otherwise False.

        """
        return self._active and self._quantity > 0

    def activate(self):
        """
        Activate the products
        """
        self._active = True

    def deactivate(self):
        """
        Deactivate the product
        """
        self._active = False

    def show(self) -> str:
        """
        Returns a string that representations the product.
        """
        return f"Product(name={self._name},price={self._price}, quantity={self._quantity})"


    def buy(self, quantity) -> float:
        """
        Buy the given amount of quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            Returns the total price (float) of the purchase.

        Raises:
            ValueError Exception if the amount of the product not available

        """
        if quantity > self._quantity:
            raise ValueError("The provided amount is not available")
        if not self._active:
            raise ValueError("The product is not active")
        total_price = quantity * self._price
        self._quantity -= quantity
        return total_price


if __name__ == "__main__":

    bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product(name="MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    print(bose.set_quantity(1000))
    print(bose.show())




