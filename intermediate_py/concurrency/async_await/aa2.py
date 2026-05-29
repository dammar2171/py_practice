import asyncio

class AsyncDownloader:
  def __init__(self,name):
    self.name = name
    self.downloads = []

  async def download(self,filename,size):
    print(f"{self.name} downloading {filename}")
    await asyncio.sleep(size)
    self.downloads.append(filename)
    print(f"{self.name} done: {filename}")
    return filename
  
  async def download_all(self,files):
    tasks = [self.download(f,s) for f,s in files]
    results = await asyncio.gather(*tasks)
    return results
  
async def main():
  downloader = AsyncDownloader("my_downloader")

  files = [
    ("photo.jpg",1),
    ("video.mp4",3),
    ("document.pdf",2),
    ("music.mp3",1),
  ]

  results = await downloader.download_all(files)
  print(f"RESULT: {results}")

asyncio.run(main())