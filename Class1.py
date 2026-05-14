# Exersise one
# class Person:
#   def __init__(self,name,age,city):
#     self.name=name
#     self.age=age
#     self.city=city
  
#   def greet(self):
#     print( f"Hi! I am {self.name}, I am {self.age} years old from {self.city}")

# p1 = Person("Dammar",23,"MNR")
# p2 = Person("Nirmala",25,"DDL")
# p3 = Person("Dheeraj",22,"KTM")

# p1.greet()
# p2.greet()
# p3.greet()


# exersise two
# class Rectangle:
#   def __init__(self,length,breadth):
#     self.length=length
#     self.breadth=breadth
#   def area(self):
#     return self.length*self.breadth
#   def perimeter(self):
#     return 2*(self.length+self.breadth)
#   def __str__(self):
#     return f"area of rectangle is {self.area()} and perimeter is {self.perimeter()}"

# rect1 = Rectangle(10,40)
# rect2 = Rectangle(50,60)

# rectangles = [rect1,rect2]

# for r in rectangles:
#   print(r)

# exersise three
class BankAccount:
  def __init__(self,initial_balance):
    self.__balance = initial_balance
    self.__history = []

  def deposit(self):
    depo_balance = int(input("enter amount for deposit: "))
    if depo_balance > 0:
      self.__balance += depo_balance
      print(f"{depo_balance} is added sucessfully!")
      self.__history.append(f"deposit:{depo_balance}")
    else:
      print("Deposit amount must be in positive number!")

  def withdrawn(self):
    withdrawn_balance = int(input("enter amount for withdrawn: "))
    if(withdrawn_balance < self.__balance):
      self.__balance -= withdrawn_balance
      print(f"{withdrawn_balance} is withdrawn sucessfully!")
      self.__history.append(f"withdrawn:{withdrawn_balance}")
    else:
      print("Insufficient amount to withdrawn!")

  def get_balance(self):
    print(f"your current balance is {self.__balance}")

  def view_history(self):
    for entry in self.__history:
      print(entry) 
    print(f"Current Balance : {self.__balance}")
print("#"*25,"Bank Account","#"*25)
p1 = BankAccount(1000)
while True:
  print("1.Deposit 2.Withdrawn 3. View Balance 4.Transaction History 5.Exit")
  option = int(input("enter your option: "))
  if option ==1 :
    p1.deposit()
  elif option ==2:
    p1.withdrawn()
  elif option ==3:
    p1.get_balance()
  elif option ==4:
    p1.view_history()
  elif option ==5:
    break
  else:
    print("invalid choice! please try again")

