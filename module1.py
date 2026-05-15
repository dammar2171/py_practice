# exersise one
# import math
# def area_circle(radius):
#   area = math.pi*(radius**2)
#   print(f"Area of circle is: {area}")
#   round_up = math.ceil(area)
#   round_down = math.floor(area)
#   print(f"Round Up : {round_up} and Round Down : {round_down}")

# def circumference_circle(radius):
#   circumference = 2 * math.pi * radius
#   print(f"Circumfererence of a circle is {circumference}")

# area_circle(5)
# circumference_circle(5)


# exersise two
import random

def roll_dice():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  return {"dice1":dice1,"dice2":dice2}

def show_value(value):
  both_sum = value["dice1"] + value["dice1"]
  print(f"Dice 1: {value["dice1"]} and Dice 2 : {value["dice1"]}")
  return both_sum

def check_result(total):
  if total ==12 :
    return "JACKPOT! 🎰"
  elif total == 2:
    return "Snake Eyes! 🐍"
  else:
    return "Try again! 😊"
while True:
  option = input("Do you want to roll dice:(yes/no)")
  if option.upper() == "YES":
    both_roll_value = roll_dice()
    both_sum = show_value(both_roll_value)
    print(check_result(both_sum))
  elif option.upper() == "NO":
    break
  else:
    print("please enter yes or no only!")
