# class BankAccount:
#   def __init__(self,owner,balance):
#     self.owner = owner
#     self.__balance = balance

#   @property
#   def balance(self):
#     return self.__balance
  
#   @balance.setter
#   def balance(self,balance):
#     if balance < 0:
#       print("Balance cannot be negative!")
#     else:
#       self.__balance = balance
#       print(f"Balance updated {balance}")
#       return self.__balance
    
# b1 = BankAccount("Dammar",50000)
# print(b1.balance)

# b1.balance = 12000
# print(b1.balance)


# using @propert.setter and @propert.deleter
class User:
  def __init__(self,name,email):
    self.name = name
    self.__email = email
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self,new_email):
    if "@" not in new_email:
      print("incorrect email!")
    else:
      self.__email = new_email
      print("Email updated!")
      return self.__email
  @email.deleter
  def email(self):
    self.__email = None
    return self.__email
  
u1 = User("Dammar","dammarbhatt111@gmail.com")
print(u1.email)
u1.email = "bhatt111@gmail.com"
print(u1.email)
u1.email = "dammar.com"
del u1.email
print(u1.email)

  