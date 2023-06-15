import os

def oddNumbers(l, r):
    result = []
    for num in range(l, r+1):
        if num % 2 != 0:
            result.append(num)
    return result


print(oddNumbers(1, 59))
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     l = int(input(3).strip())
#     r = int(input(9).strip())
#
#     result = oddNumbers(l, r)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
def findind_odd(l, r):

    list_of_num = []

    for num in range(l, r + 1):
        if num % 2 != 0:
            list_of_num.append(num)

    return list_of_num

print(findind_odd(30, 99))
