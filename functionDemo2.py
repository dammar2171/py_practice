
def check_balace(balance):
  print(f'your balance is {balance}')
def deposit(balance,amount):
  new_balance = balance+amount
  print(f'your new balace is {new_balance}')
def withdrawn(balance,amount):
  if balance > amount:
    new_amount = balance-amount
    print(f'{amount} is  withdrawn and new balance is {new_amount}')
  else:
    print("insufficient balance!")
initial = 1
while initial >0:
  balance=5000
  print("welcome to atm")
  option = int(input("enter your option (1.deposit 2.balance check 3.withdrawn 4.exit)"))
  if option == 1:
    amount = int(input("enter amount for deposit:"))
    deposit(balance,amount)
  elif option == 2:
    check_balace(balance)
  elif option == 3:
    amount = int(input("enter amount for withdrawl"))
    withdrawn(balance,amount)
  elif option == 4:
    break
  initial +=1