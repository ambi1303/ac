def legend(a, p):
    # Compute the Legendre symbol (a/p) using Euler's criterion.
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def primefactor(a):
    # Factorizes the number 'a' into its prime factors.
    factors = {}
    for d in range(2, a + 1):
        while a % d == 0:
            factors[d] = factors.get(d, 0) + 1
            a //= d
        if a == 1:
            break
    return factors

def jacobi(a, b):
    # Computes the Jacobi symbol (a/b) by factorizing b
    # and using the multiplicative property of the Legendre symbol.
    factors = primefactor(b)
    result = 1
    for p, e in factors.items():
        result *= legend(a, p) ** e
    return result

if __name__ == "__main__":
    print("Jacobi Symbol Calculator")
    try:
        a = int(input("Enter integer a: "))
        b = int(input("Enter positive odd integer b: "))
        
        # Check that b is a positive odd integer.
        if b <= 0 or b % 2 == 0:
            print("Error: b must be a positive odd integer.")
        else:
            res = jacobi(a, b)
            print(f"The Jacobi symbol ({a}/{b}) is: {res}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
