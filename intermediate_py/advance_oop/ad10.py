from abc import ABC,abstractmethod
class Shape(ABC):
   @abstractmethod
   def area(self):
      pass
   def perimeter(self):
      pass
   def describe(self):
      return f"{self.__class__.__name__}"
   
class Circle(Shape):
   def __init__(self,radius):
      self.radius = radius
   def area(self):
      import math
      return round(math.pi * self.radius**2,2)
   def perimeter(self):
      import math
      peri = 2*math.pi*self.radius
      return 
class Rectangle(Shape):
   def __init__(self,l,b):
      self.lenght = l
      self.bredth = b
   def area(self):
      return self.lenght*self.bredth
   def perimeter(self):
      return 2*(self.lenght+self.bredth)
class Triangle(Shape):
   def __init__(self,a,b,c,height):
      self.a = a
      self.b = b
      self.c = c
      self.height = height
   def area(self):
      base = self.a
      return 0.5*base*self.height
   def perimeter(self):
      return self.a+self.b+self.c
   
shapes = [
   Circle(10),
   Rectangle(10,20),
   Triangle(10,12,14,11)
]

for shape in shapes:
   print(f"Class Name: {shape.describe()}")
   print(f"Area : {shape.area()}")
   print(f"Perimeter: {shape.perimeter()}")
   