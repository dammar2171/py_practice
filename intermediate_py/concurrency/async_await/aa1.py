# Basic example of aync/await
# import asyncio

# async def greet(name,delay):
#   print(f"Good morning, {name}")
#   await asyncio.sleep(delay)
#   print(f"Good bye!, {name}")

# asyncio.run(greet("Dammar",3))



# Multiple async tasks

import asyncio
import time

async def fetch_data(source,delay):
  print(f"Data fetching from : {source}")
  await asyncio.sleep(delay)
  print(f"Data fetched from: {source}")
  return f"Data from {source}"

async def main():
  start = time.time()

  results = await asyncio.gather(
    fetch_data("Database",3),
    fetch_data("website",2),
    fetch_data("Computer",1)
  )

  end = time.time()
  print(f"Results: {results}")
  print(f"Time taken : {end-start:.2f}")

asyncio.run(main())
