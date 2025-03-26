import random

# Function to compute the Jacobi Symbol (a/n)
def jacobi_symbol(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd number")

    result = 1
    while a != 0:
        while a % 2 == 0:  # Applying properties of the Jacobi symbol
            a //= 2
            if n % 8 in [3, 5]:
                result = -result

        a, n = n, a  # Reciprocity property
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n

    return result if n == 1 else 0


def solovay_strassen(n, a):
    if n < 2:
        return False 
    if n in (2, 3):
        return True  
    if n % 2 == 0:
        return False  

    
    j_symbol = jacobi_symbol(a, n) % n 

   
    mod_exp = pow(a, (n - 1) // 2, n)

    # If they don't match, n is composite
    if j_symbol != mod_exp:
        return "Composite"

    return "Probably Prime"

n = int(input("Enter the number to test for primality: "))
a = int(input(f"Enter a random number < {n}: "))

result = solovay_strassen(n, a)
print(f"Result: {result}")