import multiprocessing
import time

def square(n):
  time.sleep(0.5)
  s = n*n
  return s

if __name__ == "__main__":
  numbers = [1,2,3,4,5,6,7,8,9,10]

  with multiprocessing.Pool(processes=4) as pool:
    result = pool.map(square,numbers)

  print(result)
