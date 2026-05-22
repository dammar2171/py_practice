# len and Contains
class Classroom:
  def __init__(self,name):
    self.name = name
    self.students = []
  def add_student(self,student):
    return self.students.append(student)
  def __len__(self):
    return len(self.students)
  def __contains__(self,name):
    return name in self.students
  
c = Classroom("class10")
c.add_student("dammar bhatt")
c.add_student("dipesh awasthi")
c.add_student("deepak giri")

print(len(c))
print("dammar bhatt" in c)
print("dammar" in c)