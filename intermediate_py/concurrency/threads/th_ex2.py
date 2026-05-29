import threading
import time

def make_dough(order):
  print(f"Dough preparing : {order}")
  time.sleep(3)
  print(f"Dough prepared : {order}")
  
def add_toppings(order):
  print(f"Add topping: {order}")
  time.sleep(2)
  print(f"Added topping: {order}")

def bake_pizza(order):
  print(f"Pizza baking: {order}")
  time.sleep(4)
  print(f"Pizza baked : {order}")

def process_pizza(order):
  make_dough(order)
  add_toppings(order)
  bake_pizza(order)

# without using threading
start = time.time()
for i in range(1,4):
  process_pizza(f"pizza{i}")
end = time.time()

print(f"Time taken: {end-start:.2f}")

# using threading
threads = []
start = time.time()
for i in range(1,4):
  t = threading.Thread(target=process_pizza,args=(f"pizza{i}",))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

end = time.time()
print(f"Time taken: {end-start:.2f}")