import requests

# Session → reuses connection → faster!
# Good when making many requests to same server

with requests.Session() as session:
    # Set headers once for all requests
    session.headers.update({
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    })

    # All requests use same session
    r1 = session.get("https://jsonplaceholder.typicode.com/posts/1")
    r2 = session.get("https://jsonplaceholder.typicode.com/posts/2")
    r3 = session.get("https://jsonplaceholder.typicode.com/posts/3")

    print(r1.json()["title"])
    print(r2.json()["title"])
    print(r3.json()["title"])