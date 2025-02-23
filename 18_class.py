class Car:
   owner = "Sinan"
   num_of_cars = 0
   def __init__(self, model, year, color, for_sale): #Constructor
      self.model = model
      self.year = year
      self.color = color
      self.for_sale = for_sale
      Car.num_of_cars +=1

   def drive(self):
      print(f"You are driving {self.color} {self.model}")

   def stop(self):
      print(f"{self.color} {self.model} has stopped")

   def describe(self):
      print(f"{self.year} {self.color} {self.model}")

class racecar(Car):
   def nitro(self):
      print(f"Nitro boost applied to {self.name}")

car1 = Car("BMW", "2024", "Red", False)
car2 = Car("Corvette", "2023", "Blue", True)
car3 = Car("Swift", "2015", "White", True)
racecar1= racecar("F1", "2021", "Black", False)
print(f"Owner: {Car.owner}\nNumber of cars: {Car.num_of_cars}")

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car1.stop()

car3.stop()

car1.describe()
car2.describe()
car3.describe()

racecar1.describe()
racecar1.drive()
racecar1.stop()