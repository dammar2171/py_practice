# Error handling with apis

import requests


def fetch_post(postID):
  try: 
   response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{postID}",timeout=5)

   response.raise_for_status()

   return response.json()
  
  except requests.exceptions.Timeout:
    print("Request timeout!")
    return None
  except requests.exceptions.ConnectionError:
    print("No internet connection!")
    return None
  except requests.exceptions.HTTPError as e:
    print("HTTP Error: ",e)
    return None
  except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")

post = fetch_post(1)
print(post)

if post :
  print(f"Title:", post['title'])