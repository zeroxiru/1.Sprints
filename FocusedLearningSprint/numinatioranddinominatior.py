def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("The division by zero to  denominator to numerator is not allowed")
        return  None
num1 = 430
num2 = 0

print_result = divide_numbers(num1, num2)
print(print_result)



write a program that  prompts the user o enter a file name and prints the content of the file using the read_file  function. handle any exception
that may occur  during the input process  or the file reading operation. print the file if it is sucessful or an appropritate  error message for an exception