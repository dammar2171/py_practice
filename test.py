# Exersise one
# class Person:
#   def __init__(self,name,age,city):
#     self.name=name
#     self.age=age
#     self.city=city
  
#   def greet(self):
#     print( f"Hi! I am {self.name}, I am {self.age} years old from {self.city}")

# p1 = Person("Dammar",23,"MNR")
# p2 = Person("Nirmala",25,"DDL")
# p3 = Person("Dheeraj",22,"KTM")

# p1.greet()
# p2.greet()
# p3.greet()


# exersise two
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
  def perimeter(self):
    return 2*(self.length+self.breadth)
  def __str__(self):
    return f"area of rectangle is {self.area()} and perimeter is {self.perimeter()}"

rect1 = Rectangle(10,40)
rect2 = Rectangle(50,60)

rectangles = [rect1,rect2]

for r in rectangles:
  print(r)