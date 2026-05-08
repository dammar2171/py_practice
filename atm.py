run = 1
while run > 0:
  print("************** WELCOME TO  ATM MACHINE ****************")
  balance = 5000
  print("Select your option (1. Check Balance  2. Withdraw  3. Exit)")
  option = int(input())
  if option == 1:
    print(balance)
  elif option == 2:
    withdraw = int(input("enter balance you want to withdrawn:"))
    if withdraw > balance:
      print("insufficient balance!")
    else:
      print(f'{withdraw} $ withdrawn sucessfully!')
  elif option == 3:
      break 
  else:
    print("invalid choice!")
  run = run +1
  