# Employee salary system
from functools import reduce
employees = [
    {"name": "Dammar",  "dept": "IT",      "salary": 85000, "years": 3},
    {"name": "Ramesh",  "dept": "HR",      "salary": 55000, "years": 7},
    {"name": "Sita",    "dept": "IT",      "salary": 92000, "years": 5},
    {"name": "Hari",    "dept": "Finance", "salary": 70000, "years": 2},
    {"name": "Gita",    "dept": "HR",      "salary": 48000, "years": 9},
    {"name": "Ram",     "dept": "IT",      "salary": 110000,"years": 8},
    {"name": "Bishnu",  "dept": "Finance", "salary": 63000, "years": 4},
    {"name": "Sunita",  "dept": "IT",      "salary": 78000, "years": 6},
]

raise_salary = list(map(lambda d : d["salary"]*1.13 if d["dept"] == "IT" else d["salary"] ,employees))

# filter_employee = filter(lambda d : d["salary"] > 70000,employees)
# for sal in filter_employee:
#   print(f"{sal["name"]}:{sal["salary"]}")

# experienced_employee = filter(lambda d: d["years"] > 5,employees)
# for e in experienced_employee:
#   print(f"{e["name"]}:{e["years"]}")

sort = sorted(employees, key=lambda d: d["salary"] ,reverse=True)

grouped_deparment = {dept:[d["name"] for d in employees if d["dept"]==dept] for dept in {p["dept"] for p in employees}}

grouped_detail = {dept:[d for d in employees if d["dept"]==dept] for dept in {p["dept"] for p in employees}}

highest_salary_per_dept = {
    dept: max(grouped_detail[dept], key=lambda d: d["salary"])
    for dept in grouped_detail
}
# for dept,emp in highest_salary_per_dept.items():
  # print(f"{dept} → {emp['name']} with salary {emp['salary']}")

total_salary_expense = reduce(lambda acc,d: acc + d["salary"] ,employees,0)
# print(total_salary_expense)

average_salary_per_dept = {dept:sum(d["salary"] for d in grouped_detail[dept])/len(grouped_detail[dept]) for dept in grouped_detail}
# for dept,avg in average_salary_per_dept.items():
#   print(f"{dept}:{avg}")

employee_eligible_promotion = list(filter(lambda d: d["years"] > 5 and d["salary"] < 70000, employees))
# for emp in employee_eligible_promotion:
#   print(emp)

employe_rank_salary = sorted(employees, key=lambda d: d["salary"] ,reverse=True)
print(70*"=")
print("Rank",5*" ","Name",5*" ","Department",5*" ","Salary",5*" ","Year")
print(70*"=")
i = 1
for emp in employe_rank_salary:
  print(f"{i}{12*" "}{emp["name"]}{12*" "}{emp["dept"]}{12*" "}{emp["salary"]}{12*" "}{emp["years"]}")
  i= i+1