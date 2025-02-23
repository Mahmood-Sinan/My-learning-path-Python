pi = 3.14159

def square(x):
   return x**2

def cube(x):
   return x**3

def compare(day):
   match day.upper():
      case "SUNDAY": 
         return "It is sunday!"
      case "MONDAY": 
         return "It is monday!"
      case "TUESDAY": 
         return "It is tuesday!"
      case "WEDNESDAY": 
         return "It is wednesday!"
      case "THURSDAY": 
         return "It is thursday!"
      case "FRIDAY": 
         return "It is friday!"
      case "SATURDAY": 
         return "It is saturday!"
      case _:
         return "Enter a valid day"
