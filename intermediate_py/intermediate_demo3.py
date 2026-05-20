# Data analysis tool 
# import json
# def add_student_data(name,english,math,science):
#   entry = {"name":name,"english":english,"math":math,"science":science}
#   try:
#     with open("students1.json","r") as file:
#       student = json.load(file)
#   except:
#     student = []
#   student.append(entry)
#   with open("students1.json","w") as file:
#     json.dump(student,file,indent=4)

# def get_students():
#   try:
#     with open("students1.json","r") as file:
#       students = json.load(file)
#       return students
#   except:
#     print("file not found!")

# def total_average(students):
#   total_marks = map(lambda s : (s["english"]+s["math"]+s["science"]),students)
#   marks_detail = []
#   for t in total_marks :
#     average = t/3
#     marks_detail.append({"total":t,"average":average})
#   return marks_detail

# def failed_student(students):
#   failed = filter(lambda s: s['english']<40 or s['math']<40 or s['science'] <40,students)
#   failed_list = []
#   for f in failed:
#     failed_list.append(f)
#   return failed_list

# def rank_student(students):
#   rank = sorted(students, key=lambda s: s["english"]+s["math"]+s["science"] ,reverse=True)
#   rank_list = []
#   for r in rank:
#     total = r["english"]+r["math"]+r["science"]
#     rank_list.append({"name":r["name"],"total":total})
#   return rank_list

# def a_students(students):
#    a_students = [s["name"] for s in students if s["english"]>80 and s["math"]>80 and s["science"]>80]
#    a_grade = []
#    for s in a_students:
#      a_grade.append(s) 
#    return a_grade


# any_failed = any(s["math"] < 40 or s["science"] < 40 or s["english"] < 40 for s in students)

# all_passed = all(s["math"] >= 40 and s["science"] >= 40 and s["english"] >= 40 for s in students)

# students = get_students()

# print(a_students(students))
# print(rank_student(students))
# print(failed_student(students))
# print(total_average(students))

# while True:
#   print("Data analysis tool")
#   print("1.Veiw all data 2. Class Performance 3. Report Card")
#   option = int(input("enter your options:"))
#   if option == 1:
#     name = input("enter your name:")
#     english = int(input("enter marks in english subject: "))
#     math = int(input("enter marks in math subject: "))
#     science = int(input("enter marks in science subject: "))
#     add_student_data(name,english,math,science)
#     print("data submited successfully!")

#   else:
#     print("invalid choice!")







from functools import reduce

# --- Step 1: Student Data ---
students = [
    {"name": "Asha", "math": 85, "science": 78, "english": 92},
    {"name": "Bikash", "math": 35, "science": 60, "english": 40},
    {"name": "Sita", "math": 70, "science": 88, "english": 75},
    {"name": "Ram", "math": 90, "science": 95, "english": 85},
    {"name": "Kiran", "math": 55, "science": 45, "english": 60},
    {"name": "Maya", "math": 80, "science": 82, "english": 78},
]

# --- Step 2: Use map → calculate total and average ---
def add_totals(s):
    total = s["math"] + s["science"] + s["english"]
    avg = total / 3
    s["total"] = total
    s["average"] = avg
    return s

students = list(map(add_totals, students))

# --- Step 3: Use filter → find students who failed any subject (<40) ---
failed_students = list(filter(lambda s: s["math"] < 40 or s["science"] < 40 or s["english"] < 40, students))

# --- Step 4: Use sorted → rank students by average ---
ranked_students = sorted(students, key=lambda s: s["average"], reverse=True)

# --- Step 5: Use comprehension → list of students who got A in all (>=80 in all subjects) ---
a_students = [s["name"] for s in students if s["math"] >= 80 and s["science"] >= 80 and s["english"] >= 80]

# --- Step 6: Use any/all → check class performance ---
any_failed = any(s["math"] < 40 or s["science"] < 40 or s["english"] < 40 for s in students)
all_passed = all(s["math"] >= 40 and s["science"] >= 40 and s["english"] >= 40 for s in students)

# --- Step 7: Print full report card ---
print("\n--- Report Card ---")
for s in students:
    print(f"{s['name']} → Math: {s['math']}, Science: {s['science']}, English: {s['english']}, Total: {s['total']}, Average: {s['average']:.2f}")

print("\n--- Failed Students ---")
if failed_students:
    for f in failed_students:
        print(f"{f['name']} failed in at least one subject")
else:
    print("No failures!")

print("\n--- Ranked by Average ---")
for i, r in enumerate(ranked_students, start=1):
    print(f"Rank {i}: {r['name']} → Average: {r['average']:.2f}")

print("\n--- Students with A in all subjects ---")
print(a_students if a_students else "None")

print("\n--- Class Performance ---")
print("Any failed:", any_failed)
print("All passed:", all_passed)
