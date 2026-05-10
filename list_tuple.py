# first exersise

# fav_movies = ["dangal","krish","game of thrones","viking"]
# length = len(fav_movies)
# print(fav_movies[0])
# print(fav_movies[length-1])
# print(length)

# second exersise 
# num = [5, 3, 8, 1, 9, 2, 7]
# print(max(num))
# print(min(num))
# print(sum(num))
# num.sort()
# print(num)


# third exersise
# names=[]
# for i in range(1,6):
#   name = input(f"enter {i} name: ")
#   names.append(name)

# for i,name in enumerate(names):
#   print(f"{i+1} : {name}")  


# exersise four 
# person = ("dammar",23,"mnr","nepal")

# name ,age,city,country = person
# print(f'name: {name}')
# print(f'age: {age}')
# print(f'city: {city}')
# print(f'country: {country}')

# exersise five
def add_cart(product):
  cart_list.append(product)

def remove_product(index):
  cart_list.pop(index) 

def show_product():
  print(cart_list)

cart_list = []
isCart_running = True
while isCart_running :
  print("choose option:")
  option = int(input("1.add 2.remove 3.show 4.exit"))
  if option == 1:
    product_add = input("enter product for add: ")
    add_cart(product_add)
  elif option == 2:
    product_index = int(input("enter product index that you want to remove"))
    remove_product(product_index)
  elif option == 3:
    show_product()
  elif option == 4:
    isCart_running = False
  else:
    print("invalid choice")


