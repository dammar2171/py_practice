# # School Management System
# from abc import ABC,abstractmethod
# import itertools
# import json

# class Person(ABC):
#   def __init__(self,name):
#     self.name = name
#   @abstractmethod
#   def get_role(self):
#     pass
#   @abstractmethod
#   def get_info(self):
#     pass
#   def __str__(self):
#     return f"Class: {self.__class__.__name__} and Role: {self.get_role()}"
#   def __eq__(self, other):
#     if isinstance(other,Person):
#       return self.name == other.name
#     if isinstance(other,str):
#       return self.name == other
    
# class Teacher(Person):
#   def __init__(self, name,subject,salary):
#     super().__init__(name)
#     self.subject = subject
#     self._salary = None
#     self.salary = salary

#   @property
#   def salary(self):
#     return self._salary 
  
#   @salary.setter
#   def salary(self,new_salary):
#     if new_salary < 0:
#       raise ValueError("Salary must be positive!")
#     self._salary = new_salary

#   def rate_student(self,student,marks):
#     student.add_marks(self.subject,marks)
  
#   def get_role(self):
#     return "Teacher"
  
#   def get_info(self):
#     return {
#      "name":self.name,
#      "subject":self.subject,
#      "salary":self.salary
#     }

# class Student(Person):
#   random_roll = itertools.count(1)
#   def __init__(self, name):
#     super().__init__(name)
#     self.subjects = {}
#     self.roll = next(Student.random_roll)

#   def __getitem__(self, subject):
#     return self.subjects.get(subject,"Not found!")
  
#   def __setitem__(self, subject, value):
#     self.subjects[subject] = value

#   def add_marks(self,subject,marks):
#     if marks < 0 or marks >100:
#       raise ValueError("marks should be between 0 - 100")
#     self.subjects[subject] = marks

#   def get_role(self):
#     return "Student"
  
#   @property
#   def average(self):
#     if not self.subjects:
#       return 0
#     return sum(self.subjects.values())/len(self.subjects)
  
#   @property
#   def grade(self):
#     avg = self.average
#     if 90 <= avg <= 100:
#       return "A+"
#     elif 80 <= avg < 90:
#       return "A"
#     elif 70 <= avg < 80:
#       return "B+"
#     elif 60 <= avg < 70:
#       return "B"
#     elif 50 <= avg < 60:
#       return "C+"
#     elif 40 <= avg < 50:
#       return "C"
#     elif 30 <= avg < 40:
#       return "D"
#     else:
#       return "Fail"
    
#   def get_info(self):
#     return {
#       "name":self.name,
#       "roll":self.roll,
#       "subjects":self.subjects,
#       "average":self.average,
#       "grade":self.grade
#     }
    
# class School:
#   def __init__(self,name):
#     self.name = name 
#     self.teacher_list = []
#     self.student_list = []

#   def add_teacher(self,teacher):
#     return self.teacher_list.append(teacher)
  
#   def add_student(self,student):
#     return self.student_list.append(student)
  
#   def find_student(self,roll):
#     for s in self.student_list:
#       if s.roll == roll:
#         return s
#     return None
#   def top_student(self,n):
#     return sorted(self.student_list, key=lambda s: s.average, reverse=True)[:n]
  
#   def subject_topper(self,subject):
#     topper = [s for s in self.student_list if subject in s.subjects]
#     if not topper:
#       return None
#     return max(topper, key=lambda s: s[subject])
  
#   def save_json(self,filename="school.json"):
#     data = {
#       "name":self.name,
#       "teachers":[t.get_info() for t in self.teacher_list],
#       "students":[s.get_info() for s in self.student_list]
#     }
#     with open(filename,"w") as file:
#       json.dump(data,file,indent=4)

#   def load_from_json(self):
#     try:
#       with open("school.json","r") as file:
#         data = json.load(file)
#         self.name = data["name"]
#         self.teacher_list = [Teacher(**t) for t in data["teachers"]]
#         self.student_list = []
#         for s in data["students"]:
#           student = Student(s["name"])
#           student.roll = s["roll"]
#           student.subjects = s["subjects"]
#           self.student_list.append(student)
#     except FileNotFoundError:
#       print("file does not found!")

# def main():
#   school = School("My School")
#   school.load_from_json()

#   while True:
#     print("\n--- School Management System ---")
#     print("1. Add Teacher")
#     print("2. Add Student")
#     print("3. Rate Student")
#     print("4. View Student Info")
#     print("5. Top Students")
#     print("6. Subject Topper")
#     print("7. Save & Exit")

#     try:
#       option = int(input("enter your option: "))
#     except ValueError:
#       print("Only enter number between 1-7.")
    
#     try:
#       if option == 1:
#         name = input("Enter teacher name: ")
#         subject = input("Enter subject name: ")
#         salary = int(input("Enter teacher salary: "))
#         school.add_teacher(Teacher(name,subject,salary))
#       elif option == 2:
#         name = input("Enter student name: ")
#         school.add_student(Student(name))
#       elif option == 3:
#         roll = int(input("Enter roll number: "))
#         subject = input("enter your subject: ")
#         marks = int(input("Enter your marks: "))
#         student = school.find_student(roll)
#         teacher = next((t for t in school.teacher_list if t.subject == subject),None)
#         if student and teacher:
#           teacher.rate_student(student,marks)
#         else:
#           print("Teacher or Student not found")
#       elif option == 4:
#         roll = int(input("Enter roll number to find student info: "))
#         student = school.find_student(roll)
#         if student :
#           print(student.get_info())
#         else:
#           print("Student not found!")
#       elif option == 5:
#         num = int(input("How many top students?"))
#         for s in school.top_student(num):
#           print(s.get_info())
#       elif option == 6:
#         subject = input("Enter subject name: ")
#         topper = school.subject_topper(subject)
#         if topper:
#           print(f"Topper in subject:{topper.name} with{topper[subject]} marks")
#       elif option == 7:
#         school.save_json()
#         break
#       else:
#         print("invalid option ,please enter correct option!")

#     except Exception as e:
#       print("ERROR: ",e)

# if __name__ == "__main__":
#   main()






"""
School Management System
Concepts: Abstract Classes, Magic Methods, Properties, Generators, JSON Save/Load
"""

import json
import os
from abc import ABC, abstractmethod


# ─── Roll Number Generator ───────────────────────────────────────────────────
def roll_generator(start=1001):
    """Auto-generates roll numbers like 1001, 1002, 1003..."""
    num = start
    while True:
        yield num
        num += 1

_roll_gen = roll_generator()


# ─── Abstract Base Class ──────────────────────────────────────────────────────
class Person(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.get_info() == other.get_info()


# ─── Teacher Class ────────────────────────────────────────────────────────────
class Teacher(Person):

    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary  # uses property setter

    # --- salary property with validation ---
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number.")
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    def get_role(self):
        return "Teacher"

    def get_info(self):
        return {"name": self.name, "subject": self.subject, "salary": self._salary}

    def rate_student(self, student, subject, marks):
        """Teacher gives marks to a student in a subject."""
        if not isinstance(student, Student):
            raise TypeError("Expected a Student object.")
        student.add_marks(subject, marks)
        print(f"✅ {self.name} gave {marks} marks to {student.name} in {subject}.")

    def __str__(self):
        return f"👨‍🏫 Teacher: {self.name} | Subject: {self.subject} | Salary: Rs.{self._salary}"


# ─── Student Class ────────────────────────────────────────────────────────────
class Student(Person):

    def __init__(self, name):
        self.name = name
        self.roll = next(_roll_gen)   # auto-generated roll number
        self._subjects = {}           # {subject: marks}

    # --- __getitem__ and __setitem__ for subjects dict ---
    def __getitem__(self, subject):
        if subject not in self._subjects:
            raise KeyError(f"Subject '{subject}' not found.")
        return self._subjects[subject]

    def __setitem__(self, subject, marks):
        self.add_marks(subject, marks)

    def add_marks(self, subject, marks):
        if not isinstance(marks, (int, float)):
            raise TypeError("Marks must be a number.")
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100.")
        self._subjects[subject] = marks

    @property
    def average(self):
        if not self._subjects:
            return 0.0
        return round(sum(self._subjects.values()) / len(self._subjects), 2)

    @property
    def grade(self):
        avg = self.average
        if avg >= 90:   return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B+"
        elif avg >= 60: return "B"
        elif avg >= 50: return "C"
        elif avg >= 40: return "D"
        else:           return "F"

    def get_role(self):
        return "Student"

    def get_info(self):
        return {"name": self.name, "roll": self.roll, "subjects": self._subjects}

    def __str__(self):
        return (f"🎓 Student: {self.name} | Roll: {self.roll} | "
                f"Avg: {self.average} | Grade: {self.grade}")


# ─── School Class ─────────────────────────────────────────────────────────────
class School:

    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    # --- Add / Find ---
    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Only Teacher objects allowed.")
        self.teachers.append(teacher)
        print(f"✅ Teacher '{teacher.name}' added.")

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects allowed.")
        self.students.append(student)
        print(f"✅ Student '{student.name}' added (Roll: {student.roll}).")

    def find_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                return s
        return None

    def top_students(self, n=3):
        if not self.students:
            print("No students yet.")
            return []
        sorted_students = sorted(self.students, key=lambda s: s.average, reverse=True)
        return sorted_students[:n]

    def subject_topper(self, subject):
        eligible = [s for s in self.students if subject in s._subjects]
        if not eligible:
            print(f"No students have marks in '{subject}'.")
            return None
        return max(eligible, key=lambda s: s._subjects[subject])

    # --- Save / Load JSON ---
    def save_to_json(self, filename="school_data.json"):
        data = {
            "school_name": self.name,
            "teachers": [t.get_info() for t in self.teachers],
            "students": [
                {
                    "name": s.name,
                    "roll": s.roll,
                    "subjects": s._subjects
                }
                for s in self.students
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Data saved to '{filename}'.")

    def load_from_json(self, filename="school_data.json"):
        if not os.path.exists(filename):
            print(f"❌ File '{filename}' not found.")
            return

        with open(filename, "r") as f:
            data = json.load(f)

        self.name = data["school_name"]
        self.teachers = []
        self.students = []

        for t in data["teachers"]:
            teacher = Teacher(t["name"], t["subject"], t["salary"])
            self.teachers.append(teacher)

        for s in data["students"]:
            student = Student.__new__(Student)
            student.name = s["name"]
            student.roll = s["roll"]
            student._subjects = s["subjects"]
            self.students.append(student)

        print(f"📂 Data loaded from '{filename}'.")


# ─── Menu Driven Program ──────────────────────────────────────────────────────
def print_menu():
    print("""
╔══════════════════════════════════════╗
║      SCHOOL MANAGEMENT SYSTEM        ║
╠══════════════════════════════════════╣
║  1. Add Teacher                      ║
║  2. Add Student                      ║
║  3. Add Marks to Student             ║
║  4. Find Student by Roll             ║
║  5. Show All Students                ║
║  6. Show All Teachers                ║
║  7. Top N Students                   ║
║  8. Subject Topper                   ║
║  9. Save Data to JSON                ║
║ 10. Load Data from JSON              ║
║  0. Exit                             ║
╚══════════════════════════════════════╝
""")


def main():
    school_name = input("Enter School Name: ").strip() or "Demo School"
    school = School(school_name)
    print(f"\n🏫 Welcome to {school.name}!\n")

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        # ── 1. Add Teacher ──
        if choice == "1":
            try:
                name    = input("Teacher Name: ").strip()
                subject = input("Subject: ").strip()
                salary  = float(input("Salary: "))
                school.add_teacher(Teacher(name, subject, salary))
            except (ValueError, TypeError) as e:
                print(f"❌ Error: {e}")

        # ── 2. Add Student ──
        elif choice == "2":
            try:
                name = input("Student Name: ").strip()
                school.add_student(Student(name))
            except Exception as e:
                print(f"❌ Error: {e}")

        # ── 3. Add Marks ──
        elif choice == "3":
            try:
                roll    = int(input("Student Roll Number: "))
                student = school.find_student(roll)
                if not student:
                    print("❌ Student not found.")
                    continue
                subject = input("Subject: ").strip()
                marks   = float(input("Marks (0-100): "))
                student.add_marks(subject, marks)
                print(f"✅ Marks added for {student.name}.")
            except (ValueError, TypeError, KeyError) as e:
                print(f"❌ Error: {e}")

        # ── 4. Find Student ──
        elif choice == "4":
            try:
                roll    = int(input("Enter Roll Number: "))
                student = school.find_student(roll)
                if student:
                    print(student)
                    print("  Subjects:", student._subjects)
                else:
                    print("❌ Student not found.")
            except ValueError:
                print("❌ Roll number must be a number.")

        # ── 5. Show All Students ──
        elif choice == "5":
            if not school.students:
                print("No students added yet.")
            else:
                print("\n── All Students ──")
                for s in school.students:
                    print(s)

        # ── 6. Show All Teachers ──
        elif choice == "6":
            if not school.teachers:
                print("No teachers added yet.")
            else:
                print("\n── All Teachers ──")
                for t in school.teachers:
                    print(t)

        # ── 7. Top N Students ──
        elif choice == "7":
            try:
                n    = int(input("How many top students? "))
                tops = school.top_students(n)
                if tops:
                    print(f"\n── Top {n} Students ──")
                    for i, s in enumerate(tops, 1):
                        print(f"{i}. {s}")
            except ValueError:
                print("❌ Enter a valid number.")

        # ── 8. Subject Topper ──
        elif choice == "8":
            subject = input("Enter Subject Name: ").strip()
            topper  = school.subject_topper(subject)
            if topper:
                print(f"🏆 Topper in {subject}: {topper.name} "
                      f"with {topper._subjects[subject]} marks")

        # ── 9. Save ──
        elif choice == "9":
            fname = input("Filename (default: school_data.json): ").strip()
            school.save_to_json(fname if fname else "school_data.json")

        # ── 10. Load ──
        elif choice == "10":
            fname = input("Filename (default: school_data.json): ").strip()
            school.load_from_json(fname if fname else "school_data.json")

        # ── 0. Exit ──
        elif choice == "0":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()