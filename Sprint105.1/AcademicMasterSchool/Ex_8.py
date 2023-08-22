def single_calculation():
    data = input("What do you want to calculate? ")
    num1 = int(data[0])
    num2 = int(data[2])
    op = data[1]

    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '/':
        res = num1 / num2
    elif op == '*':
       res = num1 * num2
    elif op == '~':
       res = num1 // num2
       remainder = num1 % num2

    print(f"The answer is {res}")
    if op == '~':
       print(f"The remainder is {remainder}")


def main():
    print("Welcome to the Python calculator!")

    n_calculations = int(input("How many calculations do you want to do? "))
    for i in range(n_calculations):
        single_calculation()


if __name__ == "__main__":
    main()
