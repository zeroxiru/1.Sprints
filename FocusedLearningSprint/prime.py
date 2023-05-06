def is_divisible_by(number, by):
    return number % by == 0
  # Remove the "pass" and add here your code

def is_prime(number):
    if number == 2:
        return True
    elif number < 2 or is_divisible_by(number, 2):
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if is_divisible_by(number, i):
            return False
    return True
def primes_in_range(start, end):
    for number in range(start+1, end):
      if is_prime(number):
         print(number)



def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print(primes_in_range(start, end))
    print(is_prime(45))
    print(is_prime(55))
    print(is_prime(51))
    print(is_prime(31))
    print(is_prime(5))
    print(is_prime(451))
    print(f"Is 10 divided by 2? {is_divisible_by(101, 2)}")
    print(f"Is 10 divided by 3? {is_divisible_by(10, 3)}")
    print(f"Is 20 divided by 11? {is_divisible_by(20, 11)}")

if __name__ == "__main__":
    main()