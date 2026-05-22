# Square,even prime generator

# def square_gen(n):
#   i = 1
#   while i <= n:
#     yield i*i
#     i += 1

# square = square_gen(10)
# for s in square:
#   print(s)

# def even_gen(n):
#   i = 2
#   while i <=n:
#     yield i
#     i +=2
# even = even_gen(100)
# for e in even:
#   print(e)


def prime_gen(n):
  def is_prime(num):
    if num < 2:
      return False
    for i in range(2,int(num**0.5)+1):
      if num%i==0:
        return False
    return True
  for i in range(1,n+1):
    if is_prime(i):
      yield i

prime = prime_gen(10)
for p in prime:
  print(p)
  
