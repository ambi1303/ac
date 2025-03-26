def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Function to compute modular inverse using Fermat’s Theorem (a^(p-2) % p)
def mod_inverse(a, p):
    return pow(a, p - 2, p)  # Since p is prime, a^(-1) ≡ a^(p-2) mod p

def encrypt(P, p, e1, e2, r):
    c1 = mod_exp(e1, r, p)  
    c2 = (P * mod_exp(e2, r, p)) % p  
    return c1, c2

def decrypt(c1, c2, d, p):
    c1_d_inv = mod_inverse(mod_exp(c1, d, p), p)  
    P = (c2 * c1_d_inv) % p  
    return P


p = int(input("Enter prime number p: "))
e1 = int(input(f"Enter base e1 (primitive root of {p}): "))
d = int(input("Enter private key d: "))
r = int(input("Enter random number r: "))

e2 = mod_exp(e1, d, p)
print(f"Public Key: (p={p}, e1={e1}, e2={e2})")
print(f"Private Key: d={d}")

P = int(input(f"Enter plaintext (less than {p}): "))

c1, c2 = encrypt(P, p, e1, e2, r)
print(f"Ciphertext: (c1={c1}, c2={c2})")

decrypted_P = decrypt(c1, c2, d, p)
print(f"Decrypted Plaintext: {decrypted_P}")
