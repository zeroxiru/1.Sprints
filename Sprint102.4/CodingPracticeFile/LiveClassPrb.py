def print_numbers_in_range(start, end):
    sum_nums = 0
    for num in range(start, end + 1):
        print(num)
        sum_nums += num
    return sum_nums

def main():
     print_numbers_in_range(2, 5)
     print(f"The sum of the num is: {sum_nums}")


if __name__ == "__main__":
    main()