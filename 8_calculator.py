print("*******************************\nWelcome to calculator programme\n*******************************")
operator = input("Enter a operation ( + - * / ): ")
if(operator == "+"):
   num1=float(input("Enter first number: "))
   num2=float(input("Enter second number: "))
   print(f"Sum: {num1+num2}")
elif(operator == "-"):
   num1=float(input("Enter first number: "))
   num2=float(input("Enter second number: "))
   print(f"Difference: {num1-num2}")
elif( operator == "*"):
   num1=float(input("Enter first number: "))
   num2=float(input("Enter second number: "))
   print(f"Product: {round(num1*num2,3)}")
elif( operator == "/"):
   num1=float(input("Enter first number: "))
   num2=float(input("Enter second number: "))
   if(num2==0):
      print("Division by zero is not defined")
   else:
      print(f"Quotient: {round(num1/num2,3)}")
else:
   print("Enter a valid operator")

print("Thank you")