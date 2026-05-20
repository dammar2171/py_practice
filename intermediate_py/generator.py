# def gen_counter(start,end):
#   current = start
#   while current <= end:
#     yield current
#     current += 1
# for num in gen_counter(1,10):
#   print(num)

# fibbonaccic series
# def fibo_series():
#   a,b=0,1
#   while True:
#     yield a
#     a,b=b,a+b
# fibo = fibo_series()
# for _ in range(10):
#   print(next(fibo) ,end=" ")


# OTP Generation
import random
def otp_generate():
  while True:
    yield random.randint(10000,99999)
otp = otp_generate()

print(next(otp))
print(next(otp))
print(next(otp))
print(next(otp))
