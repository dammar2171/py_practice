class Circle:
  def __init__(self,radius):
    self.__radius = radius
  @property
  def radius(self):
    return self.__radius
  @property
  def area(self):
    import math
    return round(math.pi *(self.__radius**2),2)
  @property  # Getter → access like variable not method!
  def circumference(self):
    import math
    return round(2 * math.pi * (self.__radius**2),2)
  
c1 = Circle(4)
print(c1.radius) #call like this without ()bracket
print(c1.area)
print(c1.circumference)