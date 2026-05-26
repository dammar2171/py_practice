# Threads example
import threading
import time

def task1():
  print("task one started.....")
  time.sleep(1)
  print("task one ended.........")

def task2():
  print("task two started..........")
  time.sleep(3)
  print("task two ended.....")

start = time.time()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Time taken: {end-start:.2f} sec")