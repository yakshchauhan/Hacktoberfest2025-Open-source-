def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Enter the upper limit: "))
prime_list = [x for x in range(2, limit + 1) if is_prime(x)]

print("Prime numbers list:", prime_list)
