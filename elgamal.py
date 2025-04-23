# Simple ElGamal Cryptosystem in Python

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
        raise ValueError("Modular inverse does not exist")
    return x % m

# Key generation
# Choose a large prime p and a generator g of the multiplicative group modulo p.
# Private key x: random in [1, p-2]
# Public key y = g^x mod p

def generate_keys(p, g, x):
    y = pow(g, x, p)
    return (p, g, y), x  # public, private

# Encryption
# Given public key (p, g, y) and message m < p, choose random k in [1, p-2]
# c1 = g^k mod p, c2 = m * y^k mod p

def encrypt(public, m, k):
    p, g, y = public
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

# Decryption
# Given private key x and ciphertext (c1, c2)
# m = c2 * (c1^x)^{-1} mod p

def decrypt(private, public, ciphertext):
    p, g, y = public
    x = private
    c1, c2 = ciphertext
    s = pow(c1, x, p)
    m = (c2 * modinv(s, p)) % p
    return m

if __name__ == '__main__':
    # Example usage with user input
    p = int(input("Enter prime p: "))
    g = int(input(f"Enter generator g (mod {p}): "))
    x = int(input(f"Enter your private key x (1 <= x < {p-1}): "))

    public, private = generate_keys(p, g, x)
    print(f"Public key (p, g, y): {public}")

    m = int(input(f"Enter plaintext m (0 <= m < {p}): "))
    k = int(input(f"Enter random k for encryption (1 <= k < {p-1}): "))

    ciphertext = encrypt(public, m, k)
    print(f"Ciphertext (c1, c2): {ciphertext}")

    decrypted = decrypt(private, public, ciphertext)
    print(f"Decrypted message: {decrypted}")
