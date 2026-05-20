from functools import reduce
products = [
    {"name": "Laptop", "price": 80000, "category": "Electronics"},
    {"name": "Phone",  "price": 45000, "category": "Electronics"},
    {"name": "Shirt",  "price": 1500,  "category": "Clothing"},
    {"name": "Pants",  "price": 2000,  "category": "Clothing"},
    {"name": "Book",   "price": 500,   "category": "Education"},
    {"name": "Tablet", "price": 35000, "category": "Electronics"},
]

def calculate_tax(product):
  tax_prices = list(map(lambda p : p["price"] * 0.13 ,product))
  return tax_prices

def filter_product(product):
  filtered_product = list(filter(lambda p : p["price"] < 50000,product))
  return filtered_product

def product_sort(products):
  sorted_list = sorted(products,key= lambda p : p["price"], reverse=True)
  return sorted_list

def group_category(products):
    grouped = {cat:[p for p in products if p['category'] == cat] for cat in {p['category'] for p in products} }
    return grouped

def expensive_product(products):
   expensive = max(products, key=lambda p: p["price"])
   return expensive

def total_value(products):
   total = reduce(lambda acc,p : acc+p["price"],products,0)
   return total

print(calculate_tax(products))
print(filter_product(products))
print(product_sort(products))
print(expensive_product(products))
print(group_category(products))
print(total_value(products))