# Decorator = adds extra feature to a function without changing original function!

# def my_decorator(func):
#   def wrapper():
#     print("decorator started!")
#     func()
#     print("decorater ended!")
#   return wrapper
# @my_decorator
# def greet():
#   print("hello sir")
# greet()

# def my_decorator(func):
#   def wrapper(*args,**kwargs):
#     print("Starting....")
#     result = func(*args,**kwargs)
#     print("Ending.....")
#     return result
#   return wrapper

# @my_decorator
# def add(a,b):
#   print(f"The sum of {a} and {b} is {a+b}")
#   return a+b
# @my_decorator
# def greet(name):
#   print(f"Good morning, {name}!")

# add(40,50)
# greet("Dammar")


# Timer decorator:

# import time
# def function_time(func):
#   def wrapper(*args,**kwargs):
#     start = time.time()
#     result = func(*args,**kwargs)
#     end = time.time()
#     print(f"{func.__name__} took {end-start:.4f} seconds")
#     return result
#   return wrapper

# @function_time
# def slow_function():
#   time.sleep(2)
#   print("function done!")

# @function_time
# def add(a,b):
#   time.sleep(1)
#   print(f"sum of {a} and {b} is {a+b}")
#   return a+b
# slow_function()
# add(6,7)

# Logger decorator
# from datetime import datetime
# def logger(func):
#   def wrapper(*args,**kwargs):
#     date = datetime.now().strftime("%D-%M-%Y,%H:%M:%S")
#     print(f"function name:{func.__name__} : {date}")
#     print(f"Arguments:{args},{kwargs}")
#     result = func(*args,**kwargs)
#     print("Results :",result)
#     return result
#   return wrapper

# @logger
# def greet(name):
#   print("Good morning,",name)

# @logger
# def add(a,b):
#   print(f"sum of {a} and {b} is {a+b}")
#   return a+b

# greet("dammar")
# add(45,67)

# validator decorator
import math
def my_validator(func):
  def wrapper(*args,**kwargs):
    for arg in args:
      if isinstance(arg ,(int,float)) and arg < 0:
        print(f"{arg} is negative number")
        return None
    return func(*args,**kwargs)
  return wrapper

@my_validator
def square_root(n):
  square = math.sqrt(n)
  print(f"Square of {n} : {square}")
  return square

square_root(10)
square_root(-10)  
      