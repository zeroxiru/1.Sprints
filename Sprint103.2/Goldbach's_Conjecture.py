def is_sum_0f_two_primes(number):
    if number % 2 == 1:
        return False
    for i in range(2, number):
        is_a_prime = True
    # check if i is a prime
        x = 2
        while x < i:
            if i % x == 0:
                is_a_prime = False
            x += 1
        if is_a_prime:
      # i is a prime, now check if j=x-i is prime
            j = number-i

            if j >= 2:

        #j must be greater or equal 2 to be prime
                good2 = True
        x = 2
        while x < j:
            if j % x == 0:
                good2= False

        x += 1
        if good2:
          print(f"The number {number} equals to the sum of {i} and {j}")
    return True


given_number = int(input("Enter a number:"))
is_sum_0f_two_primes(given_number)
