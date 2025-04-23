import random
from math import gcd

p = 11                  
d = 3                   
e1 = 2                  
e2 = pow(e1, d, p)     
m = 7                   

# Signature Generation
while True:
    r = random.randint(2, p - 2)
    if gcd(r, p - 1) == 1:
        break

C1 = pow(e1, r, p)               
r_inv = pow(r, -1, p - 1)       
C2 = (r_inv * (m - d * C1)) % (p - 1)  

print("---- ElGamal Digital Signature ----")
print(f"Message: {m}")
print(f"Signature: (C1 = {C1}, C2 = {C2})")

# Signature Verification
lhs = pow(e1, m, p)                             
rhs = (pow(e2, C1, p) * pow(C1, C2, p)) % p     

print("\n---- Verification ----")
print(f"LHS (e1^m mod p): {lhs}")
print(f"RHS (e2^C1 * C1^C2 mod p): {rhs}")

if lhs == rhs:
    print(" Signature is VALID")
else:
    print("Signature is INVALID")