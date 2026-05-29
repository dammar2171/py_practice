import requests

# Fetch data from API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check status
print(response.status_code)    # 200 = success

# Get JSON data
data = response.json()
print(data)