from datetime import date

def birthday_checker(year,month,day):
  birth_date = date(year, month, day)
  today_date = date.today()
  age = show_age(birth_date,today_date)

  print(f"Age is {age}")
  print(day_until_birthday(birth_date,today_date))
  if birth_date.month == today_date.month and birth_date.day == today_date.day:
    print("Happy Birthday ❤️")

def show_age(b_date,t_date):
  age = t_date.year - b_date.year
  if (t_date.month, t_date.day) < (b_date.month, b_date.day):
        age -= 1
  return age

def day_until_birthday(b_date,t_date):
    next_bday = date(t_date.year, b_date.month, b_date.day)

    if next_bday < t_date:
        next_bday = date(t_date.year + 1, b_date.month, b_date.day)

    day_left = (next_bday - t_date).days
    return f"Days left to come next bday is {day_left}"
 
birthday_checker(2006,12,16)
