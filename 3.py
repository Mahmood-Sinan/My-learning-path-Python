print("Welcome to calculate the area of the rectangle programme")
length=float(input("Enter the length of the rectangle in cm: "))
breadth=float(input("Enter the breadth of the rectangle in cm: "))
print(f"The rectangle has length: {length} cm and breadth: {breadth} cm and area: {length*breadth} cm²") # ' ²' is typed by turn numlock on, then alt + 0178
if length==breadth:
   print("It is a square!")