class Money:
  def __init__(self,amount):
    self.amount = amount

  def __add__(self, other):
    return self.amount + other.amount
  def __sub__(self, other):
    return self.amount - other.amount
  def __mul__(self,factor):
    return self.amount*factor
  def __str__(self):
    return "RS 500"
  def __call__(self):
    return round(self.amount / 133,2)

m1 = Money(1000)
m2 = Money(500)
print(m1 + m2)   
print(m1 - m2)   
print(m1 * 2)    
print(m1())     