# Login based decorator
# is_logged_in = False

# def login_required(func):
#   def wrapper(*args,**kwargs):
#     if not is_logged_in:
#       print("Please logged in first!")
#       return None
#     return func(*args,**kwargs)
#   return wrapper

# @login_required
# def dashboard():
#   print("hello dashboard!")

# dashboard()
# is_logged_in = True
# dashboard()


# we can apply multiple decorator
# Decorators apply bottom to top
def bold(func):
  def wrapper(*args,**kwargs):
    print("Start.........")
    func(*args,**kwargs)
    print("Ending.........")
  return wrapper

def logger(func):
  def wrapper(*args,**kwargs):
    print(f"Running:{func.__name__}")
    func(*args,**kwargs)
  return wrapper

@bold
@logger
def greet(name):
  print(f"Hello,{name}")

greet("Dammar Bhatt")