def is_prime(number):
    """
    Verify if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    x = 2
    while x < number:
        if number % 2 == 0:
            return False
        x += 1
    return True


def is_sum_of_two_primes(number):
    """
    Check if a number can be expressed as the sum of two prime numbers.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number can be expressed as the sum of two prime numbers, False otherwise.
    """
    if number % 2 == 1:
        return False

    for i in range(2, number // 2 + 1):
        if is_prime(i):
            j = number - i
            if j >= 2 and is_prime(j) and i + j == number:
                print(f"The number {number} equals the sum of {i} and {j}")

    return True


while True:
    try:
        Number = int(input("Enter a number: "))
        is_sum_of_two_primes(Number)
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")
