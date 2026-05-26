import time

def task1():
  print("task one started....")
  time.sleep(1)
  print("task one ended....")

def task2():
  print("task two started....")
  time.sleep(2)
  print("task two ended....")

start = time.time()
task1()
task2()
end = time.time()
print(f"Total time taken :{end-start:.2f}s")