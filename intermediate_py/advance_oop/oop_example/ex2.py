# PLAYLIST SYSTEM
class Song:
  def __init__(self,title,artist,duration):
    self.title = title
    self.artist = artist
    self.duration = duration

  @property
  def duration_str(self):
    min,sec = divmod(self.duration,60)
    return f"{min:02}:{sec:02}"
  
  def __str__(self):
    return f"{self.title} --> {self.artist}({self.duration_str})"
  
  def __eq__(self, value):
    return self.title == value.title and self.artist == value.artist
  
  def __lt__(self, other):
    return self.duration < other.duration
  
class Playlist:
  def __init__(self,name):
    self._name = name
    self._songs = []
  def __len__(self):
    return len(self._songs)
  def __contains__(self, item):
    return any(song.title.lower() == item.lower() for song in self._songs)
  def __getitem__(self, index):
    return self._songs[index]
  
  def __add__(self, other):
    if isinstance(other, Playlist):
        new_playlist = Playlist(self._name + " + " + other._name)
        new_playlist._songs = self._songs + other._songs
        return new_playlist
    raise TypeError("Can only add Playlist to Playlist")
    
  def __str__(self):
    return f"Playlist Name: {self._name} and total song : {len(self._songs)} "

  @property
  def total_duration(self):
    total = 0
    for song in self._songs:
       total += song.duration
    min,sec = divmod(total,60)
    return f"{min}:{sec}"
  
  @property
  def longest_song(self):
    return max(self._songs) if self._songs else None
  
  @property
  def shortest_song(self):
    return min(self._songs) if self._songs else None
  
  def add_song(self,song):
    return self._songs.append(song)
  
  def remove_song(self, title):
    for song in self._songs:
        if song.title.lower() == title.lower():
            self._songs.remove(song)
            print(f"Song removed {song.title}")
            return
    print("Song not found!")

  def short_by_duration(self):
     self._songs.sort()

  def sort_by_title(self):
    self._songs.sort(key=lambda x : x.title.lower())

  def search(self,keyword):
    return [s for s in self._songs if keyword in s.title.lower() or keyword in s.artist.lower()]
  
s1 = Song("Shape of You", "Ed Sheeran", 240)
s2 = Song("Believer", "Imagine Dragons", 210)
s3 = Song("Thunder", "Imagine Dragons", 190)

pl = Playlist("my_favorite_playlist")
pl.add_song(s1)
pl.add_song(s2)
pl.add_song(s3)
# print(pl)

# print(s1.duration_str)
# print(len(pl))

# print("Believer" in pl)      
# print("Random Song" in pl)  
# print(pl[1]) 

# print("Longest:", pl.longest_song)  
# print("Shortest:", pl.shortest_song) 

# pl.sort_by_title
# for song in pl._songs:
#   print(song)

# pl.short_by_duration
# for song in pl._songs:
#   print(song)

# results = pl.search("Imagine")
# for song in results:
#   print(song)

pl.remove_song("Believer")  
pl.remove_song("Unknown")    
