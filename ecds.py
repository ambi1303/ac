import random

a, b, p = 0, 7, 13
Gx, Gy = 5, 1  
n = 19         

d = 3

def mod_inverse(a, p):
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return None

def point_add(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return point_double(x1, y1)
    lam = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return x3, y3

def point_double(x1, y1):
    lam = ((3 * x1 * x1 + a) * mod_inverse(2 * y1, p)) % p
    x3 = (lam * lam - 2 * x1) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return x3, y3

def scalar_mult(k, x, y):
    Qx, Qy = x, y
    for _ in range(k - 1):
        Qx, Qy = point_double(Qx, Qy)
    return Qx, Qy

# --- Key Generation ---
Qx, Qy = scalar_mult(d, Gx, Gy)
print("Public Key Q = d.G =", Qx, Qy)

# --- Signing Phase ---
H = 5  
k = random.randint(1, n - 1)
Kx, Ky = scalar_mult(k, Gx, Gy)
r = Kx % n

k_inv = mod_inverse(k, n)
S = (k_inv * (H + d * r)) % n

print("\nSignature:")
print("r =", r)
print("S =", S)

# --- Verification Phase ---
w = mod_inverse(S, n)
u1 = (H * w) % n
u2 = (r * w) % n

U1x, U1y = scalar_mult(u1, Gx, Gy)
U2x, U2y = scalar_mult(u2, Qx, Qy)

Rx, Ry = point_add(U1x, U1y, U2x, U2y)
r_prime = Rx % n

print("\nVerification:")
print("r' =", r_prime)
print("Signature is", "Valid " if r_prime == r else "Invalid ")