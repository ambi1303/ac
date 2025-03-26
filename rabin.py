import math

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y

def encrypt(plain_text, n):
    return mod_exp(plain_text, 2, n)

def decrypt(cipher_text, p, q):
    n = p * q
    m1 = mod_exp(cipher_text, (p + 1) // 4, p)
    m2 = mod_exp(cipher_text, (q + 1) // 4, q)
    _, x, y = extended_gcd(p, q)
    P1 = (x * p * m2 + y * q * m1) % n
    P2 = (x * p * m2 - y * q * m1) % n
    P3 = n - P1
    P4 = n - P2
    return P1, P2, P3, P4

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
n = p * q

P = int(input(f"Enter plaintext (less than {n}): "))

C = encrypt(P, n)
print(f"Ciphertext: {C}")

possible_plaintexts = decrypt(C, p, q)
print(f"Possible Plaintexts: {possible_plaintexts}")