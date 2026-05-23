class Book:
  def __init__(self,title,author,pages,price):
    self.title=title
    self.author=author
    self.pages=pages
    self.price=price

  def __str__(self):
    return f"Book Detail: title({self.title}), author({self.author}), pages({self.pages}) and price({self.price})"
  
  def __repr__(self):
    return f"Check -- Book Detail: title({self.title}), author({self.author}), pages({self.pages}) and price({self.price})"
  
  def __len__(self):
    return self.pages
  
  def __eq__(self, other):
    if isinstance(other,Book):
      return self.title == other.title
    if isinstance(other,str):
      return self.title == other
    return NotImplemented
  
  def __lt__(self, other):
    return self.price < other.price
  
  def __gt__(self, other):
    return self.price > other.price
  
b1 = Book("jungle","dammar",400,900)
b2 = Book("computer","prabin",460,800)
b3 = Book("jungle","dammar",400,900)

collection = [b1,b2,b3]

print("jungle" in collection)
# print(repr(b2))
# print(b1 == b3)
# print(b1>b2)
# print(b1<b3)
# for c in collection:
#   print(c)

# for c in sorted(collection):
#   print(c)
