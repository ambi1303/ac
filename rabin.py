# Shortened Rabin Cryptosystem without primality tests

def egcd(a, b):
    """Extended Euclidean Algorithm"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def modinv(a, m):
    """Modular inverse of a under modulus m"""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No inverse")
    return x % m


def crt(r1, p, r2, q):
    """Combine roots via CRT for modulus n=p*q"""
    n = p * q
    inv_p = modinv(p, q)
    inv_q = modinv(q, p)
    return (r1 * q * inv_q + r2 * p * inv_p) % n


def encrypt(m, n):
    return pow(m, 2, n)


def decrypt(c, p, q):
    n = p * q
    # Compute square roots modulo p and q (p,q ≡ 3 mod 4 assumed)
    r_p = pow(c, (p + 1) // 4, p)
    r_q = pow(c, (q + 1) // 4, q)
    roots = []
    for sp in (r_p, (-r_p) % p):
        for sq in (r_q, (-r_q) % q):
            roots.append(crt(sp, p, sq, q))
    return sorted(set(roots))

if __name__ == '__main__':
    # Input primes and message
    p = int(input("Enter prime p (≡3 mod4): "))
    q = int(input("Enter prime q (≡3 mod4): "))
    n = p * q
    m = int(input(f"Enter plaintext m (0 ≤ m < {n}): "))

    # Encrypt and decrypt
    c = encrypt(m, n)
    print(f"Ciphertext: {c}")
    options = decrypt(c, p, q)
    print(f"Possible plaintexts: {options}")
