# def main():
#     total_sum_of_number = 0
#
#     for num in range(999):
#         number = int(input("Enter the Number: "))
#         total_sum_of_number += number
#
#         if total_sum_of_number >= 1000:
#             break
#
#     print(total_sum_of_number)
#
#
# if __name__ == "__main__":
#     main()
#
#

def main():
    total_sum_of_number = 0

    while True:
        num = int(input("Enter the Number:"))
        total_sum_of_number += num
        if total_sum_of_number >= 1000:
            break

    # for num in range(999):
    #     number = int(input("Enter the Number: "))
    #     total_sum_of_number += number

    #     if total_sum_of_number >= 1000:
    #         break

    print(total_sum_of_number)


if __name__ == "__main__":
    main()
