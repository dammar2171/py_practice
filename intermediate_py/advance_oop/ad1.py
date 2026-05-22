class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks

    # for user to print
  def __str__(self):
    return f"name :{self.name} and marks:{self.marks}"
  # for developer for debugging like console.log in js.
  def __repr__(self):
    return f"name = {self.name} and marks={self.marks}"
  
s = Student("dammar",89)
print(s)
print(repr(s))    #repr() we can call like this .
