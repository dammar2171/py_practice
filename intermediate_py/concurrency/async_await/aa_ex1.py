import asyncio
import time

async def get_weather(city):
  print(f"Weather is fetching of {city} city.....")
  await asyncio.sleep(1)
  print(f"Weather fetched of {city}......")
  return "35 degree"

async def get_news(heading):
  print(f"News fetching: {heading}............")
  await asyncio.sleep(2)
  print(f"news fetched : {heading}...")
  return "Accident happen at 6 o'clock"

async def get_rate(currency):
  print(f"{currency} rate fetching.....")
  await asyncio.sleep(1)
  print(f"{currency} rate fetched.....")
  return 110.67


async def main():
  start = time.time()

  results = await asyncio.gather(
    get_weather("mahendranaagr"),
    get_news("Accident"),
    get_rate("USA")
  )


  end = time.time()
  print(f"Result: {results}")
  print(f"Time taken: {end-start:.2f}s")


asyncio.run(main())

