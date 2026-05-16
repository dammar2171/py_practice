def reverse_string(str):
  reversed_string = str[::-1]
  return reversed_string

def count_vowels(str):
  count = 0
  for char in str:
    if char in ["a","e","i","o","u"]:
      count += 1
  return count

def is_pelindrome(str):
  pelindrome = str[::-1]
  if str == pelindrome:
    return "Pelindrome!"
  else:
    return "Not Pelindrome!"
  
def capitalize_word(str):
  capital = str.capitalize()
  return capital

def remove_space(str):
  return str.strip()

