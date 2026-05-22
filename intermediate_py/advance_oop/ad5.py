# make object comparable using method __eq__ , __lt__ and __gt__

class Student:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
  def __eq__(self, value):
    return self.marks == value.marks
  def __lt__(self, other):
    return self.marks < other.marks
  def __gt__(self, other):
    return self.marks > other.marks
  def __str__(self):
    return f"{self.name} and {self.marks}"
  
s1 = Student("dammar",98)
s2 = Student("nishita",99)
s3 = Student("Niru",98)

print(s1==s2)
print(s1==s3)
print(s1>s2)
print(s2>s3)

students = [s1,s2,s3]
rank = sorted(students,reverse=True)
for r in rank:
  print(r)

