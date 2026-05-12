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
def validate_password():
    password = input("enter password at least 8 character and include numbers : ")
    has_digit = any(char.isdigit() for char in password)
    if len(password) >= 8:
      if has_digit:
        print("password is valid!")
      else:
        raise ValueError("password should contain number also")
    else:
      raise ValueError("password invalid need at least 8 character!")

try:
  validate_password()
except ValueError as e:
  print(e)