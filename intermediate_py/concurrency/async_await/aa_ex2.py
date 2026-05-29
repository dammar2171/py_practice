import asyncio
import time 

async def fetch_news(source,heading,delay):
  print(f"News fectching from {source}...")
  await asyncio.sleep(delay)
  print(f"{source}:{heading} is fetched...")
  return (source,heading,delay)

async def main():
  sources = [
    ("BBC news","politics",1),
    ("CNN","economy",1.5),
    ("Reuters","sports",2),
    ("AL_zeera","Tourism",1.8),
    ("Local news","Dieases",0.5)
  ]

  # sequential 
  sq_start = time.time()
  sq_result = []
  for source,heading,delay in sources:
    result = await fetch_news(source,heading,delay)
    sq_result.append(result)
  sq_end = time.time()
  print(f"Result: {sq_result}")
  print(f"Time taken: {sq_end-sq_start:.2f}")


  # parellel execution
  p_start= time.time()
  p_results = []
  task = [fetch_news(s,h,d) for s,h,d in sources]
  results = await asyncio.gather(*task)
  p_end = time.time()
  first_source = min(results, key=lambda x: x[2])[0]

  print(f"Result: {results}")
  print(f"Time taken : {p_end-p_start:.2f}")

  print(f"first task finished: {first_source}")

asyncio.run(main())