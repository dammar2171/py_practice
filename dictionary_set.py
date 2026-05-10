# first exersise
# person = {
#   "name":"dammar bhatt",
#   "age":23,
#   "city":"mahendranagar",
#   "hobby":"coding"
# }

# for key,value in person.items():
#   print(f'{key} : {value}')

# #second exersise
# countries = {
#   "nepal":"kathmandu",
#   "india":"delhi",
#   "america":"new york",
#   "china":"beijing",
#   "japan":"tokyo"
# }

# find_capital = input("enter country name :")
# capital = None
# for key,value in countries.items():
#   if key == find_capital:
#     capital = value

# if capital :
#   print(capital)
# else:
#   print("country not found!")


#third exersise
# students = {"Dammar": 95, "Ramesh": 88, "Sita": 92,"Nirmala":100}
# highest_mark = students["Dammar"]
# lowest_mark = students["Dammar"]
# for key,value in students.items():
#   print(f'{key} : {value}')
#   if value >= highest_mark:
#     highest_mark = value
#   else:  
#     if value <= lowest_mark:
#       lowest_mark = value

# print("highest marks is ",highest_mark)
# print("lowest marks is ",lowest_mark)

# fourth exersise
# numbers = {1, 2, 2, 3, 4, 4, 4, 5, 5}
# print(numbers)
# print(len(numbers))

# fifth exersise
# sentence = input("enter any sentence: ")
# words = sentence.split()
# word_count = {}

# for word in words:
#   if word in word_count:
#     word_count[word] += 1
#   else:
#     word_count[word] = 1

# print(word_count)


# fifth exersise
print("*******CONTACT BOOK**********")
print("1.add contact 2.search 3.delete 4.show all 5.exit")
phone_book ={}
while True:
  option = int(input("choose one option: "))
  if option == 1:
    name = input("enter name: ")
    number= input("enter nunber: ")
    phone_book[name]=number
    print("number added sucessfully!")
  elif option == 2:
    search = input("enter name to search number: ")
    if search in phone_book:
      value = phone_book.get(search)
      print(value)
    else:
      print("Name not found")
  elif option == 3:
    delete_name = input("enter name to delete number: ")
    if delete_name in phone_book:
      del phone_book[delete_name]
      print("deleted sucessfully")
    else:
      print("not fount name to delete!")
  elif option == 4:
    if phone_book:
      for key,value in phone_book.items():
        print(f'{key}:{value}')
    else:
      print("No contact found yet!")
  elif option == 5:
    break
  else:
    print("invalid option")
