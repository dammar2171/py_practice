# # ID generator program
def id_generator(prefix):
  count = 1
  while True:
    yield prefix+str(count).zfill(3)
    count +=1
  
user_id = id_generator("USR")
order_id = id_generator("ODR")
print(next(user_id))
print(next(order_id))

