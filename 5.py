import math
# print(math.sqrt(4))
# print(math.ceil(9.1))
# print(math.floor(8.9))
# print(math.pi)
# print(math.e)

print("Welcome to calculating the circumference of a circle")
r = float(input("Enter the radius of the circle in cm: "))
circumference = 2 * math.pi * r
print(f"The circumference of the circle with {r} is {round(circumference,3)} cm")