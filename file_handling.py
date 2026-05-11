# exersise one
# with open("diary.txt","w") as file:
#   for i in range(3):
#     text = input(f"enter {i+1} word: ")
#     line = text + "\n"
#     file.write(line)

# with open("diary.txt","r") as file:
#   data = file.read()
#   print(data)


# exersise two
# with open("diary.txt","a") as file:
#   for i in range(2):
#     text = input(f"enter {i+1} word: ")
#     line = text + "\n"
#     file.write(line)
# with open("diary.txt","r") as file:
#   data = file.read()
#   print(data)


# exersise third
# import csv
# students = [
#   ["name","marks"],
#   ["dammar",90],
#   ["nirmala",98],
#   ["prabin",89],
#   ["dheeraj",93],
# ]
# with open("students.csv",'w', newline="") as file:
#   w = csv.writer(file)
#   w.writerows(students)

# with open("students.csv","r") as file:
#   print(file.read())

# exersise fourth
# import json
# profile_data ={
#   "name":"dammar",
#   "age":23,
#   "city":"mahendranagar",
#   "hobbies":["coding","gaming","armwrestling"],
#   "skills":["java","python","html","css"],
# }

# with open("profile.json","w") as file:
#   json.dump(profile_data,file)

# with open("profile.json","r") as file:
#    print(json.load(file))

# exersise fifth
# import json
# import datetime

# def write_note():
#     note = input("Enter your note: ")
#     date = str(datetime.date.today())
#     entry = {"date": date, "note": note}
#     try:
#         with open("diary.json", "r") as file:
#             diary = json.load(file)
#     except FileNotFoundError:
#         diary = []
#     diary.append(entry)
#     with open("diary.json", "w") as file:
#         json.dump(diary, file, indent=4)

# def read_note():
#     try:
#         with open("diary.json", "r") as file:
#             diary = json.load(file)
#             for entry in diary:
#                 print(f"{entry['date']}: {entry['note']}")
#     except FileNotFoundError:
#         print("File not found")

# while True:
#     print("\nChoose option")
#     print("1. Write Note  2. Read Notes  3. Exit")
#     option = int(input("Choose your option: "))
#     if option == 1:
#         write_note()
#     elif option == 2:
#         read_note()
#     elif option == 3:
#         break
#     else:
#         print("Invalid option")


# exersise sixth
import json
def save_contact():
  name = input("enter name: ")
  phone = input("enter your phone number: ")
  entry = {"name":name, "phone":phone}
  try:
    with open("contact.json","r") as file:
      contact = json.load(file)
  except FileNotFoundError:
    contact = []
  contact.append(entry)

  with open("contact.json","w") as file:
    json.dump(contact,file,indent=4)

def view_contact():
  try:
    with open("contact.json","r") as file:
      contact = json.load(file)
      for entry in contact:
        print(f"{entry['name']}: {entry['phone']}")
  except FileNotFoundError:
    print("file not found!")


while True:
  print("1. Add contact 2. View_contact 3.Exit")
  option = int(input("choose your option: "))
  if option == 1:
    save_contact()
    print("contact saved sucessfully!")
  elif option == 2:
    view_contact()
  elif option == 3:
    break
  else:
    print("invalid choice")