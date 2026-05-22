class StudentData:
  def __init__(self):
    self.data={}
  def __getitem__(self, subject):
    return self.data.get(subject,"Not found!")
  def __setitem__(self, subject, value):
    self.data[subject]=value
  def __str__(self):
    return str(self.data)
  
record = StudentData()
record["math"]=78
record["science"]=89
record["english"]=90

print(record["math"])
print(record["history"])
print(record)