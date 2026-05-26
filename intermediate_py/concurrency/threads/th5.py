# Thread lock
import threading

# counter = 0
# def increment():
#   global counter
#   for _ in range(1000000):
#     counter += 1

# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(f"Count: {counter}")  might be problem 20000000


counter = 0
lock = threading.Lock()

def increment_safe():
  global counter
  for _ in range(10000000):
    with lock:
      counter += 1

t1 = threading.Thread(target=increment_safe)
t2 = threading.Thread(target=increment_safe)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Counter with lock: {counter}")