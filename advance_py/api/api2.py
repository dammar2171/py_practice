import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

data = response.json()
print(data)

print(data["name"])
print(data["email"])

# print(response.headers)
print("Content type: ",response.headers["content-type"])
print(response.text)

if response.ok:
  print("success")
else:
  print("failed")
