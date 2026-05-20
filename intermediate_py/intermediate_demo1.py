# exersise one
# cubes = [n**3 for n in range(1,10)]
# print(cubes)

# numbers = [ n for n in range(1,50) if n%3 == 0]
# print(numbers)

# marks = [78, 32, 90, 45, 15, 67, 88, 25]
# passed = ["pass" if p >= 40 else "fail" for p in marks ]
# print(passed)

# exersise two
# area_rect = lambda l,b : l*b
# print(area_rect(10,20))

# conversion = lambda km : km * 0.621
# print(f"{conversion(100)} miles")

# check_number = lambda num : "positive" if num>0 else "negative"
# print(check_number(-10))

# check_large = lambda num1,num2 : f"{num1} is greater" if num1 > num2 else f"{num2} is greater"
# print(check_large(70,30))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = list(filter(lambda n: n%2 == 0,numbers))
# square_num = list(map(lambda s: s**2,even_num))
# print(square_num)


names  = ["Dammar", "Ramesh", "Sita", "Hari"]
marks  = [95, 67, 83, 45]

dic_student = dict(zip(names,marks))
passed_student = list(filter(lambda p : p>=50,marks))
sort = list(sorted(marks))
i=1
for k,v in dic_student.items():
  print(f"{i}:{k}:{v}")
  i +=1

print(sort)
print(passed_student)
print(dic_student)