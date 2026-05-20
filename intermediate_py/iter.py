# Iters and next
# Handle iter using try and except.
# fruits = ["mango","apple","Banana","pomegranate","litch"]
# it = iter(fruits)
# while True:
#   try:
#     fruit = next(it)
#     print(fruit)
#   except StopIteration:
#     print("Not items remains!")
#     break

# Cout up
# class Count:
#   def __init__(self,start,end):
#     self.start = start
#     self.end = end

#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     if self.start > self.end:
#       raise StopIteration
#     value = self.start
#     self.start += 1 
#     return value

# count1 = Count(1,20)
# for num in count1:
#   print(num)


# Even number iterator 
class Even:
  def __init__(self,limit):
    self.current = 2
    self.limit = limit
  def __iter__(self):
    return self
  def __next__(self):
    if self.current > self.limit:
      raise StopIteration
    even = self.current 
    self.current +=2
    return even

even = Even(10)
for num in even:
  print(num)