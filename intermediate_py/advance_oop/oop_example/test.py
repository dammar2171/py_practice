name = input("enter your name: ")
print(list(filter(lambda n: n in "aeiouAEIOU" ,name)))