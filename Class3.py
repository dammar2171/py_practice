# Student Management System
import json
class Student:
  def __init__(self,name,age,marks):
    self.name = name 
    self.age = age
    self.marks = marks
    self.grade = None

  def add_student(self):
    entry = {"Name":self.name,"Age":self.age,"Marks":self.marks}
    try:
      with open("students.json","r") as file:
        details = json.load(file)
    except FileNotFoundError:
      details = []
    details.append(entry)
    with open("students.json","w") as file:
      json.dump(details,file,indent=4)

  def calculate_grade(self):
    if self.marks <= 100 and self.marks > 90:
      self.grade="A+"
    elif self.marks <= 90 and self.marks > 80:
      self.grade="A"
    elif self.marks <= 80 and self.marks > 70:
      self.grade="B+"
    elif self.marks <= 70 and self.marks > 60:
      self.grade="B"
    elif self.marks <= 60 and self.marks > 50:
      self.grade="C+"
    elif self.marks <= 50 and self.marks > 40:
      self.grade="C"
    elif self.marks <= 40 and self.marks > 30:
      self.grade="D"
    else:
      self.grade="F"

  def result(self):
    if self.grade == "A+" or self.grade == "A" or self.grade == "B+" or self.grade == "B" or self.grade == "C+" or self.grade == "C" or self.grade == "D":
      print("You are passed in exam 😊")
    elif self.grade == "F":
      print("You are failed in exam 😔")

  def topper_lower(self):
    try:
      with open("students.json","r") as file:
        details = json.load(file)
      topper = max(details, key=lambda x:x["Marks"])
      lower = min(details, key=lambda x:x["Marks"])
      print(f"Topper:{topper}")
      print(f"Lower:{lower}")
    except FileNotFoundError as e:
      print(e)

s1 = Student("dammar",23,90)
s2 = Student("Harish",22,67)
s1.add_student()
s2.add_student()
s1.calculate_grade()
s1.result()
s1.topper_lower()