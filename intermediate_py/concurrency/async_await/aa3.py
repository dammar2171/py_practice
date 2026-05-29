import asyncio

async def async_counter(start,end,delay=1):
  for i in range(start,end):
    await asyncio.sleep(delay)
    yield i

async def main():
  print("Counting:")
  async for num in  async_counter(1,7):
    print(num)

asyncio.run(main())