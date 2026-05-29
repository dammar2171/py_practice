import threading
import time 

def task(num,delay):
  print(f"Thread {num} is starting........")
  time.sleep(delay)
  print(f"Thread {num} is completed........")

# sequential
start = time.time()
for i in range(1,6):
  task(i, i*0.5)
end = time.time()
print(f"Time taken by sequential: {end-start:.2f}s")

# multithreading
threads = []
start = time.time()
for i in range(1,6):
  t = threading.Thread(target=task,args=(i,i*0.5))
  threads.append(t)
  t.start()

for t in threads:
  t.join()
end = time.time()
print(f"Time taken by threads: {end-start:.2f}s")

