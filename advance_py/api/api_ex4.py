import requests
from functools import reduce

res = requests.get("https://restcountries.com/v3.1/region/asia")
data = res.json()
# for d in data:
#   if d["region"] == "Asia":
#     print(d)
population_list = []
country_list = []
for d in data:
  population_list.append(d["population"])
  country_list.append(d["name"]["common"])

country_population = list(zip(country_list,population_list))

sorted_with_population = sorted(country_population, key= lambda x: x[1], reverse=True) 
top = 0
# for country,population in sorted_with_population:
#   print(f"{country}----> {population}")
#   top += 1
#   if top == 10:
#     break

language_in_number = []
for d in data:
  language_in_number.append(len(d["languages"]))

country_language = list(zip(country_list,language_in_number))

# for country,number_of_lang in country_language:
#   print(f"{country}---> {number_of_lang}")

area_list = []
for d in data:
  area_list.append(d["area"])

country_area = list(zip(country_list,area_list))

sort_by_area = sorted(country_area, key=lambda x: x[1])

# print("Smallest country based on area: ",sort_by_area[0])

total_population_asia = reduce(lambda acc,next: acc+next,population_list,0)

print(f"Total population of  asia: {total_population_asia}")