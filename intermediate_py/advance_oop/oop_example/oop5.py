# Library system
from abc import ABC,abstractmethod
class LibraryItem(ABC):
  def __init__(self,title):
    self.title = title

  @abstractmethod
  def checkout(self):
    pass
  @abstractmethod
  def return_items(self):
    pass
  @abstractmethod
  def info(self):
    pass
  def __str__(self):
    return f"Title:{self.title} class name: {self.__class__.__name__}"
  def __eq__(self, other):
    if isinstance(other,LibraryItem):
      return self.title == other.title
    if isinstance(other,str):
      return self.title == other
    return NotImplemented
  def __lt__(self, other):
    return self.title < other.title
  
class Book(LibraryItem):
  def __init__(self,title,author,pages,copies):
    super().__init__(title)
    self.author = author
    self.pages = pages
    self._copies = copies
  @property
  def copies(self):
    return self._copies
  @copies.setter
  def copies(self,new_copies):
    if new_copies < 0:
      raise ValueError("Copies cannot be negative")
    self._copies = new_copies
  
  def checkout(self):
    if self._copies > 0:
      self._copies -=1
      return f"Book {self.title} checkout, Remaining {self._copies} copies!"
    return f"{self.title} not available!"
  
  def return_items(self):
    self._copies +=1
    return f"Book {self.title} returned , Copies now: {self._copies}"

  def info(self):
    return f"Book :{self.title},Author:{self.author},Pages:{self.pages} and Copies:{self._copies}"

class Magazine(LibraryItem):
  def __init__(self, title,issue,month):
    super().__init__(title)
    self.issue = issue
    self.month = month
  def checkout(self):
    return f"Magazine {self.title} Issued {self.issue} checkout!"
  def return_items(self):
    return f"Magazine {self.title} returned!"
  def info(self):
    return f"Magazine {self.title}, Issued:{self.issue} and Month:{self.month}"
  
class DVD(LibraryItem):
  def __init__(self, title,duration,genre):
    super().__init__(title)
    if duration <= 0:
      raise ValueError("Duration must be positive!")
    self.duration = duration
    self.genre = genre

  def checkout(self):
    return f"DVD {self.title} and genre: {self.genre} is checkouted!"
  
  def return_items(self):
    return f"Dvd: {self.title} is returned!"
  def info(self):
    return f"DVd title : {self.title},duration:{self.duration} and genre :{self.genre}"
  
class Library:
  def __init__(self):
    self.items = []

  def add_item(self,value):
    return self.items.append(value)
  
  def search_by_title(self,title):
    return [item for item in self.items if item.title.lower() == title.lower()]

  def sort_by_field(self,field):
    return sorted(self.items, key=lambda x:getattr(x,field,None))
  
  def checkout_item(self,title):
    for item in self.items:
      if item.title.lower() == title.lower():
        return item.checkout()
    return f"{title} not found!"
    
  def return_items(self,title):
    for item in self.items:
      if item.title.lower() == title.lower():
        return item.return_items()
    return f"{title} not found!"
    
  def show_all_items(self):
    return [item.info() for item in self.items]
  
lib = Library()
b = Book("jungle","dammar",400,20)
m = Magazine("Millionare","2078-12-2",10)
d = DVD("captain america",120,"science_fiction")

lib.add_item(b)
lib.add_item(m)
lib.add_item(d)

for info in lib.show_all_items():
  print(info)

print("jungle" in lib.search_by_title("jungle"))
print(lib.checkout_item("millionare"))
print(lib.checkout_item("captain america"))
print(lib.checkout_item("jungle"))

print(lib.return_items("jungle"))
print(lib.return_items("Millionare"))

for item in lib.sort_by_field("title"):
  print(item)