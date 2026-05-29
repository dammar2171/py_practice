# UPDATE AND DELETE

import requests

update_post = {
  "id":1,
  "title":"hey budddy",
  "body":"hey i am your friend ,i will be there always with you.",
  "userId":1
}

response =  requests.put("https://jsonplaceholder.typicode.com/posts/1",json=update_post)

print(response.status_code)
print(response.text)


response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.text)