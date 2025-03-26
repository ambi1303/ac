
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)


def diffie_hellman(p, g, private_key_A, private_key_B):
    public_A = mod_exp(g, private_key_A, p)  
    public_B = mod_exp(g, private_key_B, p)  

    # Compute shared secret keys
    shared_key_A = mod_exp(public_B, private_key_A, p)  
    shared_key_B = mod_exp(public_A, private_key_B, p)  

    return public_A, public_B, shared_key_A, shared_key_B

p = int(input("Enter prime number (p): "))
g = int(input(f"Enter primitive root (g) of {p}: "))
private_key_A = int(input("Enter private key for User A: "))
private_key_B = int(input("Enter private key for User B: "))


public_A, public_B, shared_key_A, shared_key_B = diffie_hellman(p, g, private_key_A, private_key_B)

print(f"Public Key of A: {public_A}")
print(f"Public Key of B: {public_B}")
print(f"Shared Secret Key computed by A: {shared_key_A}")
print(f"Shared Secret Key computed by B: {shared_key_B}")

# Verify 
if shared_key_A == shared_key_B:
    print(f"Final Shared Secret Key: {shared_key_A}")
else:
    print("Error: Shared keys do not match!")