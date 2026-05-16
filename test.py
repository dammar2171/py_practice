import json,random
from datetime import datetime

def generate_password(text):
  random_number = str(random.randint(10000000,999999999))
  unique_password = text + random_number
  return unique_password

def password_save(psd,name,time):
  entry = {"password":psd,"name":name,"time":time}
  try:
    with open("password.json","r") as file:
      password = json.load(file)
  except FileNotFoundError:
    password = []
  password.append(entry)
  with open("password.json","w") as file:
    json.dump(password,file,indent=4)

def show_passwords():
  try:
    with open("password.json","r") as file:
      password = json.load(file)
      for p in password:
        print(f"{p['password']}")
  except FileNotFoundError as e:
    print(e)

def search_password(s_name):
  try:
    with open("password.json","r") as file:
      password = json.load(file)
      for p in password:
        if p["name"] == s_name:
          print(f"{p['password']},{p['name']},{p['time']}")
  except FileNotFoundError:
    print("No password found!")
    
def delete_password(s_name):
  try:
    with open("password.json","r") as file:
      password = json.load(file)
      password = [p for p in password if p["name"] != s_name]
      with open("password.json","w") as file:
        json.dump(password,file,indent=4)
        print("password deleted successfully!")
  except FileNotFoundError:
    print("password not found!") 
while True:
  date_time = datetime.today().strftime("%D-%M-%Y,%H:%M:%S")
  print("Password Manager Application")
  print("1. Generate password 2.Show all passwords 3.Search password 4.Delete password 5.Exit")
  option = int(input("enter your option: "))
  if option == 1:
    text = input("enter your text to generate random password: ")
    name = input("enter your service name: ")
    random_psd = generate_password(text)
    password_save(random_psd,name,date_time)
    print("password saved sucessfully!")
  elif option ==  2:
    show_passwords()
  elif option == 3:
    name = input("enter service name to search password: ")
    search_password(name)
  elif option == 4:
    name = input("enter service name to search password: ")
    delete_password(name)
  elif option == 5:
    break
  else:
    print("invalid choice please choose correct one option!")

