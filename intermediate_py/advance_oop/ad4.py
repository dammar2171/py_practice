# Cart example to understand add object
class Cart:
  def __init__(self,items=[]):
    self.items = items.copy()
  
  def __add__(self, other):
    return Cart(self.items + other.items)
  
  def __len__(self):
    return len(self.items)
  
  def __str__(self):
    return f"items: {self.items}"
    
c1 = Cart(["apple","banana","grapes"])
c2 = Cart(["pomegranate","mango"])
merged = c1 + c2

print(merged)
print(len(merged))
