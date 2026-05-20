import time
from datetime import datetime

def timer(func):
  def wrapper(*args,**kwargs):
    start = time.time()
    result = func(*args,**kwargs)
    end = time.time()
    print(f"Time takes : {(end-start)*1000} ms")
    return result
  return wrapper

def logger(func):
  def wrapper(*args,**kwargs):
    date= datetime.now().strftime("%D-%M-%Y,%H:%M:%S")
    print(f"Date:{date}")
    result = func(*args,**kwargs)
    return result
  return wrapper

def validate(func):
  def wrapper(*args,**kwargs):
    if not args and not kwargs:
      print("No arguments!")
      return None
    return func(*args,**kwargs)
  return wrapper

def id_generator(prefix="USR"):
  count = 1
  while True:
    yield f"{prefix}+{str(count).zfill(3)}"
    count +=1

user_id = id_generator("USR")
order_id = id_generator("ODR")

@timer
@logger
@validate
def create_user(name,email):
  u_id = next(user_id)
  user = {"id":u_id,"name":name,"email":email}
  print("User created sucessfully!")
  return user

@timer
@logger
@validate
def create_order(costumer,product,amount):
  o_id = next(order_id)
  order = {"id":o_id,"costumer":costumer,"product":product,"amount":amount}
  print("Order created sucessfully!")
  return order

create_user("dammar","dammarbhatt111@gmail.com")
create_order("dammar","laptop",60000)