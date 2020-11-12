import math

def calculate(a,b,c):
    try:
        x1 = ((-b)+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = ((-b)-math.sqrt(b**2-4*a*c))/(2*a)

        x1 = round(x1, 4)
        x2 = round(x2, 4)
    except Exception:
        return False
    
    print('X1= ', x1)
    print('X2= ', x2)
    return {'x1': x1, 'x2': x2}


# print("Enter A, B, C")
# print('')

# a = float(input("A: "))
# b = float(input("B: "))
# c = float(input("C: "))

# calculate(a,b,c)

