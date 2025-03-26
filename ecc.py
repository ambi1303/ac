from sympy import mod_inverse  # For computing modular inverses

class EllipticCurve:
    def __init__(self, a, b, p):
        """
        Initialize the elliptic curve: y² = x³ + ax + b (mod p)
        :param a: Coefficient a
        :param b: Coefficient b
        :param p: Prime number defining the finite field GF(p)
        """
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, P):
        """
        Check if point P = (x, y) is on the elliptic curve.
        The identity element (point at infinity) is represented as (None, None).
        """
        if P == (None, None):
            return True
        x, y = P
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def add(self, P, Q):
        """
        Add two points P and Q on the elliptic curve.
        Implements both point addition and point doubling.
        Returns the resulting point R = P + Q.
        """
        # If one of the points is the identity element, return the other.
        if P == (None, None):
            return Q
        if Q == (None, None):
            return P

        x1, y1 = P
        x2, y2 = Q

        if P == Q:
            # Point doubling: λ = (3*x1² + a) / (2*y1)
            lam_num = (3 * x1**2 + self.a) % self.p
            lam_den = (2 * y1) % self.p
        else:
            # Point addition: λ = (y2 - y1) / (x2 - x1)
            lam_num = (y2 - y1) % self.p
            lam_den = (x2 - x1) % self.p

        # Check for division by zero; if lam_den == 0, then return the identity element.
        if lam_den == 0:
            return (None, None)

        # Compute slope λ using modular inverse
        lam = (lam_num * mod_inverse(lam_den, self.p)) % self.p

        # Compute resulting point coordinates
        x3 = (lam**2 - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def multiply(self, P, n):
        """
        Perform scalar multiplication: compute Q = n * P using the double-and-add method.
        :param P: Point on the curve
        :param n: Scalar multiplier (can be negative)
        :return: The point Q = n * P
        """
        # Handle negative multipliers by computing the inverse point first.
        if n < 0:
            return self.multiply(point_inverse(P, self.p), -n)
        
        result = (None, None)  # Identity element (point at infinity)
        temp = P

        while n:
            if n & 1:
                result = self.add(result, temp)
            temp = self.add(temp, temp)
            n >>= 1
        return result

def point_inverse(P, p):
    """
    Compute the inverse (negation) of a point on the elliptic curve.
    For a point P = (x, y), the inverse is (x, -y mod p).
    The identity (None, None) is its own inverse.
    """
    if P == (None, None):
        return (None, None)
    x, y = P
    return (x, (-y) % p)

# -------------------------------------------
# Define ECC parameters and create the curve.
# Here we use a small curve for demonstration:
p = 17         # Prime field GF(17)
a, b = 2, 2    # Curve: y² = x³ + 2x + 2 (mod 17)
curve = EllipticCurve(a, b, p)

# Base point G on the curve (must satisfy the curve equation)
G = (5, 1)

# Verify G is on the curve
if not curve.is_on_curve(G):
    print("Error: Base point G is not on the curve!")
    exit()

# -------------------------------------------
# Key Generation
private_key = 7                      # User's private key (d)
public_key = curve.multiply(G, private_key)  # Public key P = d × G
print(f"Public Key: {public_key}")

# -------------------------------------------
# Encryption
# Assume the plaintext is a point on the curve.
message_point = (6, 3)
if not curve.is_on_curve(message_point):
    print("Error: Message point is not on the curve!")
    exit()

random_k = 9  # Random integer for encryption (should be chosen randomly in practice)

# Compute ciphertext:
# C1 = k × G
C1 = curve.multiply(G, random_k)
# C2 = M + k × P, where P is the public key.
C2 = curve.add(message_point, curve.multiply(public_key, random_k))
print(f"Ciphertext: C1 = {C1}, C2 = {C2}")

# -------------------------------------------
# Decryption
# To decrypt, compute M = C2 - (d × C1)
# Subtraction of a point is defined as addition of its inverse.
dC1 = curve.multiply(C1, private_key)
neg_dC1 = point_inverse(dC1, p)
decrypted_message = curve.add(C2, neg_dC1)
print(f"Decrypted Message: {decrypted_message}")

# Verify that decryption recovers the original message.
if decrypted_message == message_point:
    print("✅ Successful Decryption!")
else:
    print("❌ Decryption Error!")
