import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

json_data = response.json()

# print(json_data)


for d in json_data:
  print(f"{d["name"]} | {d["email"]} | {d["address"]["city"]} | {d["company"]["name"]}")


print("Total user:", len(json_data))