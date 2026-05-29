# Send parameters in URL
# https://jsonplaceholder.typicode.com/posts?userId=1

import requests

userId = {
  "userId":2
}

response = requests.get("https://jsonplaceholder.typicode.com/posts",params=userId)

# print(response.status_code)

# print(response.json())

# print(response.text)

print(len(response.json()))