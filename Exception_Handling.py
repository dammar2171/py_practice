# exersise one
# try:
#   num1 = int(input("enter first number: "))
#   num2 = int(input("enter second number: "))
#   div = num1/num2
# except ValueError as e:
#   print(f"Not a number! {e}")
# except ZeroDivisionError as e:
#   print(f"cannot divided by zero {e}")
# else :
#   print(f"Answer is {div}")


# exersise two
# fruits = ["apple", "banana", "mango"]
# try:
#   index = int(input("enter index number to find fruit:"))
#   print(fruits[index])
# except IndexError:
#   print("Out of range")


#exersise three
# import os 
# try:
#   # if os.path.exists("data.txt"):
#     with open("data.txt","r") as file:
#       content = file.read()
#       print(content)
#   # else:
#     # print("file not found!")
# except FileNotFoundError as e:
#   print(f"File not found!,ERROR:{e}")


# exersise four
# def validate_password():
#     password = input("enter password at least 8 character and include numbers : ")
#     has_digit = any(char.isdigit() for char in password)
#     if len(password) >= 8:
#       if has_digit:
#         print("password is valid!")
#       else:
#         raise ValueError("password should contain number also")
#     else:
#       raise ValueError("password invalid need at least 8 character!")

# try:
#   validate_password()
# except ValueError as e:
#   print(e)

# exsersise five
# import random
# random_number = random.randint(1,10)
# def start_game(random_number):
#   while True:
#     number = int(input("enter any number: "))
#     if number == random_number:
#       print("you have won!")
#       break
#     else:
#       print("try again!")
#       continue
# try:
#   start_game(random_number)
# except ValueError :
#   print("Invalid input! Enter a number!")
#   start_game(random_number)


# exersise six
import json

class InvalidMarksError (Exception):
  pass

def create_student(entry):
  try:
    with open("marks.json","r") as file:
      student = json.load(file)
  except FileNotFoundError:
      student=[]
  student.append(entry)
  with open("marks.json","w") as file:
    json.dump(student,file,indent=4)

def add_student():
  name = input("enter student name: ")
  marks = int(input("enter marks of student: "))
  if marks < 0 or marks >100:
    raise InvalidMarksError("Marks should be greater than 0 and smaller than 100!")
  else:
    entry = {"name":name,"marks":marks}
    create_student(entry)
def show_grade():
  try:
    with open("marks.json","r") as file:
      student = json.load(file)
      for data in student:
        print(f"{data['name']}:{data['marks']}")
  except FileNotFoundError as e:
    print("No student record found!")

try:
  add_student()
except InvalidMarksError as e:
  print(e)

show_grade()