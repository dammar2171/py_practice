# uppercase and repeated decorator

# def uppercase_decorator(func):
#   def wrapper(*args,**kwargs):
#     result = func(*args,**kwargs)
#     print(f"Good morning!,{result}")
#     return result
#   return wrapper
  
# @uppercase_decorator
# def greet(name):
#   return name.upper()

# greet("Dammar")


def repeat_decorator(func):
  def wrapper(*args,**kwargs):
    func(*args,**kwargs)
    func(*args,**kwargs)
    func(*args,**kwargs)
  return wrapper

@repeat_decorator
def greet(name):
  print(f"Heyy,{name}")

greet("dammar")