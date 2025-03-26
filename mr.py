import random

def miller_rabin(n, a):
    if n < 2:
        return False  
    if n in (2, 3):
        return True   
    if n % 2 == 0:
        return False 

    # Express (n - 1) as (2^k) * m
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1

    b = pow(a, m, n)

    # If b is 1 or -1 (n-1), then n is probably prime
    if b == 1 or b == n - 1:
        return "Probably Prime"

    # Keep squaring b while k > 1
    for _ in range(k - 1):
        b = pow(b, 2, n)
        if b == n - 1:
            return "Probably Prime"

    return "Composite"

n = int(input("Enter the number to test for primality: "))
a = int(input(f"Enter a random number < {n-2}: "))

result = miller_rabin(n, a)
print(f"Result: {result}")