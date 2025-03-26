def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod(e, phi_n):
    for d in range(2, phi_n):
        if (e * d) % phi_n == 1:
            return d
    return -1

if __name__ == "__main__":
    # Take user input for prime numbers and the message
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    m = int(input("Enter the message (as an integer) m: "))

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose public exponent e such that gcd(e, phi_n) == 1
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            break

    # Compute the modular inverse d (private exponent)
    d = mod(e, phi_n)
    
    # Encrypt and decrypt the message
    c = pow(m, e, n)  # Encryption: c = m^e mod n
    pt = pow(c, d, n) # Decryption: pt = c^d mod n

    # Output the results
    print(f"Original message: {m}")
    print(f"Public exponent (e): {e}")
    print(f"Private exponent (d): {d}")
    print(f"Encrypted message (c): {c}")
    print(f"Decrypted message: {pt}")
