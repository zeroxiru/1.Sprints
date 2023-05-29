def is_prime(number):
    """
    verify if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    initial_prime = 2
    while initial_prime < number:
        # checking the number is prime or not through divisible by x increment value
        if number % initial_prime == 0:
            return False
        initial_prime += 1
        #print(f"{number}   {x}")
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
    for first_num in range(2, number // 2 + 1):

        if is_prime(first_num):
            second_num = number - first_num
            if is_prime(second_num):
                print(f"The number {number} equals the sum of {first_num} and {second_num}")

    return False


def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            is_sum_of_two_primes(number)
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()

