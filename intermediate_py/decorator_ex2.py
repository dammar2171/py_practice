# Decorator System
import time
def timer(func):
  def wrapper(*args,**kwargs):
    start = time.time()
    result = func(*args,**kwargs)
    end = time.time()
    print(f"Time taken: {(end-start)*1000:.2f} ms")
    return result
  return wrapper

def logger(func):
  def wrapper(*args,**kwargs):
    t = time.time()
    print(f"Function: {func.__name__} and Time: {t}")
    result = func(*args,**kwargs)
    return result
  return wrapper

def validate(func):
  def wrapper(*args,**kwargs):
    if not args and not kwargs:
      print("No arguments found")
      return None
    return func(*args,**kwargs)
  return wrapper

@timer
@logger
@validate
def calculate_discount(price,percent):
  discount = (price/100)*percent
  print(f"Your discount amount is {discount}")
  return discount

@timer
@logger
@validate
def process_payment(amount,method):
  process = {"amount":amount,"method":method}
  print(f"amount is {amount} and method is {method}")
  return process

@timer
@logger
@validate
def create_invoice(costumer,items,total):
  print(f"costumer name is {costumer} and total price is {total}")
  for i in items:
    print(i)
  invoice = {"costumer":costumer,"items":items,"total":total}
  return invoice

calculate_discount(10000,20)
process_payment(40000,"Esewa")
create_invoice("dammar",["apple","banana","grapes"],5000)


