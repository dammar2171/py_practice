# Count down iterator
# class CountDown:
#   def __init__(self,start,end):
#     self.current = start
#     self.end = end
#   def __iter__(self):
#     return self
#   def __next__(self):
#     while self.current <= self.end:
#       raise StopIteration
#     value = self.current
#     self.current -= 1
#     return value

# count = CountDown(10,0)
# for c in count:
#   print(c) 


# Range Iterator
class MyRange:
  def __init__(self,start,end,step):
    self.current = start
    self.end = end
    self.step = step
  def __iter__(self):
    return self
  def __next__(self):
    while self.current >= self.end:
      raise StopIteration
    value = self.current
    self.current += self.step
    return value
  
value = MyRange(0,10,2)
for v in value:
  print(v)
         