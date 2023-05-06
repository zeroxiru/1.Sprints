def print_name_and_age(name: str, age: int) -> None:
    print(f"My name is {name} and I am {age} years old.")


def print_rectangle_area(length: float, width: float) -> None:
    area = length * width
    print(f"The area of the rectangle is {area}.")

def bill_amount(value: float, paid: bool) -> None:
    status = "paid" if paid else "pending"
    print(f"the value is €{value:.2f} and is {status}.")

print(print_name_and_age("Ibrahim", 32))
print(print_rectangle_area(12.2, 10))