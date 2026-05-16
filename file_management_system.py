import os,json
from datetime import datetime
def show_files():
  entries = os.listdir()
  return entries

def file_size(file_path):
  return os.path.getsize(file_path) 

def create_folder(folder_name):
  return os.mkdir(f"{folder_name}")

def log_info(entry):
  try:
    with open("log.json","r") as file:
      log = json.load(file)
  except FileNotFoundError:
    log = []
  log.append(entry)
  with open("log.json","w") as file:
    json.dump(log,file,indent=4)
    

while True:
  date_time = datetime.today()
  print("File Manager System")
  print("1.View all files 2.File size 3.Create folder 4.Exit")
  option = int(input("enter your option: "))
  if option == 1:
    print(show_files())
    entry = {"action":"view files","time":f"{date_time}"}
    log_info(entry)
  elif option == 2:
    file = input("enter file name: ")
    files = show_files()
    for f in files:
      if f == file:
        size = file_size(f)
        print(size)
        entry = {"action":"file size checked","name":size,"time":f"{date_time}"}
        log_info(entry)
  elif option == 3:
    folder = input("enter folder name that you want to create: ")
    print(create_folder(folder))
    entry = {"action": "folder created", "name":folder, "time":f"{date_time}"}
    log_info(entry)
  elif option == 4:
    break
  else:
    print("invalid choice please choose correct one option!")