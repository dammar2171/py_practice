class Laptop:
  def __init__(self,b,p,bty):
    self._brand = None
    self._price = None
    self._battery = None
    self._brand = b
    self._price = p
    self._battery = bty

  @property
  def brand(self):
    return self._brand
  
  @brand.setter
  def brand(self,new_value):
    if len(new_value) == 0 :
      raise ValueError("Brand name cannot be empty string")
    self._brand = new_value
    return self._brand

  @property
  def price(self):
    
    return self._price
  
  @price.setter
  def price(self,new_value):
    if new_value < 0:
      raise ValueError("Price must be in positive")
    self._price = new_value
    return self._price
  
  @property
  def battery(self):
    return self._battery
  
  @battery.setter
  def battery(self,new_value):
    if 1 <= new_value <= 100:
      self._battery = new_value
      return self._battery
    raise ValueError("Battery must be in between 1 to 100!")
  
  def __str__(self):
    return f"Brand: {self.brand} | Price: RS {self.price} | Battery: {self.battery}%"
  
  def __eq__(self, other):
    return self.brand == other.brand and self.price == other.price

  def __gt__(self, other):
    return self.price > other.price
  
  def __lt__(self, other):
    return self.price < other.price
  
l1 = Laptop("DELL",50000,78)
l2 = Laptop("DELL",50000,78)
l3 = Laptop("ASUS",120000,90)

merge = [l1,l2,l3]
# print(l1)
# print(l1 == l2)
# print(l1>l3)
# print(l1<l3)

# for lap in sorted(merge):
#   print(lap)

try:
  l1.battery = 300
except ValueError as e:
  print("ERROR: ",e)

try:
  l1.brand = ""
except ValueError as e:
  print("ERROR: ",e)

try:
  l1.price = -78
except ValueError as e:
  print("ERROR: ",e)
