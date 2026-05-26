# threading with argument example
import threading
import time

def file_download(filename,size):
  print(f"{filename} is downloading....")
  time.sleep(size)
  print(f"{filename} downloaded✅")

files = [("passport.txt",1),("dammar.jpg",2),("resume.pdf",4),("ironman.mp4",5)]

start = time.time()
threads = []

for filename,size in files:
  t = threading.Thread(target=file_download, args=(filename,size))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

end = time.time()

print(f"Time taken: {end-start:.2f}s")
print(f"Without threading it will take : {sum(s for _,s in files)}")

