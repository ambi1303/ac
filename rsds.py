def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def sign(message, d, n):
    return pow(message, d, n)

def verify(signature, e, n):
    return pow(signature, e, n)

if __name__ == "__main__":
    p, q = 13, 7
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 5  
    d = mod_inverse(e, phi)  

    message = 7
    print("RSA Digital Signature")
    print(f"Message: {message}")
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    signature = sign(message, d, n)
    print(f"Signature: {signature}")

    verified_message = verify(signature, e, n)
    print(f"Verified Message: {verified_message}")

    if verified_message == message:
        print("Signature is Valid")
    else:
        print("Signature is Not Valid")