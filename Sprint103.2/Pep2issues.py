# def calculate_sum(num1, num2):
#     result = num1 + num2
#     if result >= 10:  # if result is bigger or equal to 10
#         print("Result is greater than or equal to 10")
#     else:
#         print("Result is less than 10")
#     return result  # return result
#
#
# def calculate_mul(num1, num2):
#     """ Calculates result of multiplication"""
#     res_multiplication = num1 * num2
#     return res_multiplication
#
#
# def main():
#     print(calculate_sum(5, 6))
#     print(calculate_mul(3, 4))
#
#
# if __name__ == "__main__":
#     main()
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
        is_prime_i = True
        # Check if i is a prime
        x = 2
        while x < i:
            if i % x == 0:
                is_prime_i = False
            x += 1

        if is_prime_i:
            # i is a prime, now check if j = x - i is prime
            j = number - i
            if j >= 2:
                is_prime_j = True
                x = 2
                while x < j:
                    if j % x == 0:
                        is_prime_j = False
                    x += 1

                if is_prime_j:
                    print(f"The number {number} equals the sum of {i} and {j}")

    return True


while True:
    try:
        Number = int(input("Enter a number: "))
        is_sum_of_two_primes(Number)
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")

