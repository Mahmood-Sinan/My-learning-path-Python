import math
print("Welcome to calculating the hypotenuse of a right triangle")
a=float(input("Enter the side a: "))
b=float(input("Enter the side b: "))
c=math.sqrt((a**2+b**2))
print(f"The hypotenuse of a right triangle with side a: {a}, b: {b} is c: {round(c,2)}")