# import threading
# import time

# initial_balance = 10000

# def deposit(balance):
#   global initial_balance
#   for _ in range(50):
#     temp = initial_balance
#     time.sleep(0.5)
#     temp += balance
#     initial_balance = temp
#     print(f"{balance} is deposited! Now total balance is {initial_balance}")

# def withdrawn(balance):
#   global initial_balance
#   for _ in range(50):
#     temp = initial_balance
#     time.sleep(0.5)
#     temp -= balance
#     initial_balance = temp
#     print(f"{balance} is withdrawn! Now total balance is {initial_balance}")


# t1 = threading.Thread(target=deposit,args=(100,))
# t2 = threading.Thread(target=withdrawn,args=(100,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()


import threading
import time

lock = threading.Lock()
initial_balance = 10000

def deposit(balance):
  global initial_balance
  for _ in range(50):
    with lock:
      temp = initial_balance
      time.sleep(0.5)
      temp += balance
      initial_balance = temp
      print(f"{balance} is deposited! Now total balance is {initial_balance}")

def withdrawn(balance):
  global initial_balance
  for _ in range(50):
    with lock:
      temp = initial_balance
      time.sleep(0.5)
      temp -= balance
      initial_balance = temp
      print(f"{balance} is withdrawn! Now total balance is {initial_balance}")


t1 = threading.Thread(target=deposit,args=(100,))
t2 = threading.Thread(target=withdrawn,args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()