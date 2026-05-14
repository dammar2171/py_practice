# class Vechile:
#   def __init__(self,brand,speed):
#     self.brand = brand
#     self.speed = speed

#   def show_info(self):
#     print(f"Vechile brand name is {self.brand} and speed is {self.speed} km/hrs")

# class Car(Vechile):
#   def __init__(self,brand,speed,door):
#     self.door = door
#     super().__init__(brand,speed)

#   def has_doors(self):
#     print(f"Car have {self.door} door")

# class Bike(Vechile):
#   def __init__(self,brand,speed,side_car):
#     self.side_car=side_car
#     super().__init__(brand,speed)

#   def has_sidecar(self):
#     print(f"Sidecar:{self.side_car}")
    
# car1 = Car("Toyota",120,4)
# bike1 = Bike("Ninja Kawasaki",400,True)
# car1.show_info()
# car1.has_doors()
# bike1.show_info()
# bike1.has_sidecar()


# library management system using class

class Book:
  def __init__(self,title,author,year,is_available=False):
    self.title = title
    self.author = author
    self.year = year
    self.is_available = is_available
    self.borrow_book =[]

  def borrow(self):
    name = input("enter your name: ")
    book_name = input("enter book name: ")
    record = {"Name":name,"Book":book_name}
    self.borrow_book.append(record)
    print(f"You have borrowed {book_name} book!")

  def return_borrow(self):
    name = input("enter your name: ")
    book_name = input("enter book name: ")
    record = {"Name":name,"Book":book_name}
    if record in self.borrow_book:
      self.borrow_book.remove(record)
      print(f"You have returned {book_name} book!")
    else:
      print(f"This borrow record does not exist!")

class Library():
  def __init__(self):
   self.books = []

  def add_book(self,book):
    self.books.append(book)

  def search_book(self,title):
    for book in self.books:
      if book.title == title:
        print(f"{title} book found!")
  
  def show_available(self):
    for book in self.books:
      if book.is_available:
        print(book.title)
  
  def show_all(self):
    for book in self.books:
      print(book.title, book.author, book.year, book.is_available)
  
b1 = Book("hacking","dammar",2026,True)
b2 = Book("computer","dammar",2008,False)
b3 = Book("Coding","Nirmala",2078,True)
l1 = Library()
l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)
l1.show_available()
l1.show_all()
l1.search_book("hacking")