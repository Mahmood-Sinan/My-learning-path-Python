class Shape:
   def __init__(self, color, is_filled):
      self.color = color
      self.is_filled = is_filled

   def describe(self):
      print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
   def __init__(self, color, is_filled, radius):
      super().__init__(color, is_filled) #to call a funtion from parent class. When we call super(),imagine we are replacing super() with name of parent class: like super().__init__(self,...) becoming Shape.__init__(self,...)
      self.radius = radius
      
   #method overwriting

   def describe(self):
      super().describe()
      print(f"It is a circle of area of {2*3.14*self.radius*self.radius} sq.cm")

class Square(Shape):
   def __init__(self, color, is_filled, width):
      super().__init__(color, is_filled)
      self.width = width

class Triangle(Shape):
   def __init__(self, color, is_filled, width, height):
      super().__init__(color, is_filled)
      self.width = width
      self.height = height

circle = Circle(color = "red", is_filled = True, radius =  5)
square = Square(color = "blue", is_filled = False, width =  5)
triangle = Triangle(color = "yellow", is_filled = False, width =  7, height = 8)

print(circle.color)
print(circle.is_filled)
print(f"Circle radius: {circle.radius} cm")


print(square.color)
print(square.is_filled)
print(f"Square side: {square.width} cm")

print(triangle.color)
print(triangle.is_filled)
print(f"Triangle width: {square.width} cm")
print(f"Triangle height: {triangle.height} cm")

circle.describe()
square.describe()