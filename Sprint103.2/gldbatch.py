
def is_prime(number):
    """
    verify if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        return True

def is_sum_of_two_primes(number):
    """
    check if the number is sum of two prime numbers.
    Args:
        number(int): checking the interger number.
    Returns:
        bool: it returns true if the sum of two prime numbers equivalent to
        the given number. Otherwise False
    """
    if number % 2 == 1:
        return False
    prime_pairs = set()
    for i in range(2, number):

         if is_prime(i):
           # checking the second number j is prime or not.
            j = number - i

            if j >= i and is_prime(j):
                prime_pairs.add((i, j))

    for pair in prime_pairs:
        print(f"The number {number} equals the sum of {pair[0]} and {pair[1]}")



    return True


given_number = 10

is_sum_of_two_primes(given_number)


