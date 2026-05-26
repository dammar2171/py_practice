# Therading using oops way

import threading
import time

class DownloadThread(threading.Thread):
  def __init__(self, filename,size):
    super().__init__()
    self.filename = filename
    self.size = size

  def run(self):
    print(f"{self.filename} downloading....")
    time.sleep(self.size)
    print(f"{self.filename} downloaded....")

t1 = DownloadThread("myself.jpg",3)
t2 = DownloadThread("resume.pdf",4)
t3 = DownloadThread("hey.docx",1)

start = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
end = time.time()
print(f"All task done in {end-start:.2f} s")