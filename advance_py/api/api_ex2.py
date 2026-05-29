import requests
userId ={
  "userId" :1
}
response = requests.get("https://jsonplaceholder.typicode.com/todos",params=userId)

# print(response.text)

data = response.json()
print(len(data))
complete_count = 1
for d in data:
  if d["completed"]:
    complete_count += 1

pending_count = 1
for d in data:
  if not d["completed"]:
    pending_count += 1

print("Completed todos: ",complete_count)
print("Pending todos: ",pending_count)

completion_percentage = (complete_count/len(data))*100
print(f"Completion percentage is {completion_percentage}%")