if __name__ == "__main__":
    # Get user input for curve parameters and point coordinates.
    a = int(input("Enter the curve parameter a: "))
    p = int(input("Enter the prime modulus p: "))
    x1 = int(input("Enter the x-coordinate x1: "))
    y1 = int(input("Enter the y-coordinate y1: "))

    try:
        # Calculate the slope lambda for point doubling:
        # lambda = (3*x1^2 + a) / (2*y1) mod p
        lam = ((3 * x1**2 + a) * pow(2 * y1, -1, p)) % p

        # Calculate the new x and y coordinates:
        x3 = (lam**2 - 2 * x1) % p
        y3 = (lam * (x1 - x3) - y1) % p

        print("Resulting point after doubling:")
        print("x3 =", x3)
        print("y3 =", y3)
    except ValueError as e:
        # This error is raised if the modular inverse does not exist.
        print("Error during computation:", e)
