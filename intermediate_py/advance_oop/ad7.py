class Multiplier:
  def __init__(self,factor):
    self.factor = factor
     # called when object is used as function
  def __call__(self, number):
    return number*self.factor
  
double = Multiplier(2)
triple = Multiplier(3)

print(double(5)) # 10 → called like function!
print(triple(10))

# Tax calculator
class TaxCalculator:
  def __init__(self,rate):
    self.rate = rate
  def __call__(self, price):
    tax = price * self.rate/100
    total = price+tax
    return round(total,2)
  def __str__(self):
    return f"TaxCalculator({self.rate})%"

tax1 = TaxCalculator(10)

print(tax1)
print(tax1(40000))