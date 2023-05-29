def is_prime(number):
    """
    verify if a number is prime.

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