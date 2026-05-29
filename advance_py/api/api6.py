import requests

# Some APIs use API key in params
API_KEY = "your_api_key_here"

response = requests.get(
    "https://api.example.com/data",
    params={"api_key": API_KEY}
)

# Some use headers
headers = {"X-API-Key": API_KEY}
response = requests.get(
    "https://api.example.com/data",
    headers=headers
)