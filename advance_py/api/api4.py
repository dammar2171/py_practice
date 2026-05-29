# POST request 

import requests

new_post = {
  "title": "hey computer",
  "body": "i am computer and you can use me for any task",
  "userId":2
  }

response = requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post)

print(response.status_code)

print(response.text)