def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generate_keys():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)

    e = next(e for e in range(2, phi) if gcd(e, phi) == 1)
    
    d = mod_inverse(e, phi)
    return e, d, n

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

if __name__ == "__main__":
    e, d, n = generate_keys()
    print(f"\nPublic Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})\n")

    M1 = int(input("Enter first message (M1): "))
    M2 = int(input("Enter second message (M2): "))

    C1 = encrypt(M1, e, n)
    C2 = encrypt(M2, e, n)

    C_mul = (C1 * C2) % n
    decrypted_result = decrypt(C_mul, d, n)
    expected_value = (M1 * M2) % n

    print(f"\nDecrypted (C1 * C2 mod n): {decrypted_result}")
    print(f"Expected (M1 * M2 mod n): {expected_value}")

    if decrypted_result == expected_value:
        print("\n RSA Homomorphic Multiplication holds!")
    else:
        print("\n Error in homomorphic property.")