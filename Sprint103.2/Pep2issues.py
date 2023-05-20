def calculate_sum(num1, num2):
    result = num1 + num2
    if result >= 10:  # if result is bigger or equal to 10
        print("Result is greater than or equal to 10")
    else:
        print("Result is less than 10")
    return result  # return result


def calculate_mul(num1, num2):
    """ Calculates result of multiplication"""
    res_multiplication = num1 * num2
    return res_multiplication


def main():
    print(calculate_sum(5, 6))
    print(calculate_mul(3, 4))


if __name__ == "__main__":
    main()
