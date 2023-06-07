# finding the greatest common divisor of two number
list_1 = []
list_2 = []
def gcd(num1, num2):
    for i in range(1, num1):
        if num1 % i == 0:
            list_1.append(i)

    for i in range(1, num2):
        if num2 % i == 0:
            list_2.append(i)
    print(list_1, list_2)
def common_gcd_number(list_1, list_2):

   common_number = []
   for i in list_1:
       if i in list_2:
           common_number.append(i)
   return common_number


def max_gcd(com_num_list):
    if com_num_list:
        return  max(com_num_list)
    else:
        print("None")


gcd(50,100)
common_numbers = common_gcd_number(list_1, list_2)
maximum_number = max_gcd(common_numbers)

print(common_numbers)
print(maximum_number)
