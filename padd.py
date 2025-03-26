def mod_inverse(a, p):
    return pow(a, -1, p)  

def point_addition(x1, y1, x2, y2, p):
    if x1 == x2 and y1 == y2:
        return None  
    
    if x1 == x2:
        return None  # Point at infinity

    lambda_num = (y2 - y1) % p
    lambda_den = mod_inverse((x2 - x1) % p, p)  
    lam = (lambda_num * lambda_den) % p  

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return x3, y3

p = 17  


x1=int(input("Enter the value of x1:"))
y1=int(input("Enter the value of y1:"))
x2=int(input("Enter the value of x2:"))
y2=int(input("Enter the value of y2:"))

result = point_addition(x1, y1, x2, y2, p)

if result:
    x3, y3 = result
    print(f"Added Point: ({x3}, {y3})")
else:
    print("Result is the point at infinity.")