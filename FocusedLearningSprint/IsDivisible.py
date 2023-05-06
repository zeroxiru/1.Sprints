def is_divisible_by(number, by):
	return number % by ==0

def is_prime(number):
    if number ==2:
        return True
    elif number < 2 or is_divisible_by(number, 2):
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if is_divisible_by(number, i):
            return False
    return  True

print(f"Is 10 divided by 2? {is_divisible_by(1220, 2)}")
print(f"Is 10 divided by 3? {is_divisible_by(10321, 3)}")
print(f"Is 20 divided by 11? {is_divisible_by(202, 11)}")

print(is_prime(45))
print(is_prime(55))
print(is_prime(51))
print(is_prime(31))
print(is_prime(5))
print(is_prime(451))