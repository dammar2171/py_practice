# Post Manager Program
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def show_all_posts():
  try:
    response = requests.get(BASE_URL,timeout=5)
    response.raise_for_status()
    return response.text
  except requests.exceptions.ConnectTimeout:
    print("Running timeout!")
    return None
  except requests.exceptions.ConnectionError:
    print("No internet connection!")
    return None
  except requests.exceptions.HTTPError as e:
    print("HTTP_ERROR:",e)
    return None
  except requests.exceptions.RequestException as e:
    print("Something went wrong: ",e)
    return None

def single_post(id):
  Id ={
    "id":id
  }
  try:
    response = requests.get(BASE_URL,params=Id)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.ConnectTimeout:
    print("Running timeout!")
    return None
  except requests.exceptions.ConnectionError:
    print("No internet connection!")
    return None
  except requests.exceptions.HTTPError as e:
    print("HTTP_ERROR:",e)
    return None
  except requests.exceptions.RequestException as e:
    print("Something went wrong: ",e)
    return None

def create_new_post(userId,id,title,body):
  data ={
    "userId": userId,
    "id":id,
    "title":title,
    "body":body
  }
  try:
    response = requests.post(BASE_URL,json=data)
    response.raise_for_status()
    data = {
      "data": response.json(),
      "status": response.status_code
    }
    return data
  except requests.exceptions.ConnectTimeout:
    print("Running timeout!")
    return None
  except requests.exceptions.ConnectionError:
    print("No internet connection!")
    return None
  except requests.exceptions.HTTPError as e:
    print("HTTP_ERROR:",e)
    return None
  except requests.exceptions.RequestException as e:
    print("Something went wrong: ",e)
    return None
  
def update_post(id,title,body):
  data ={
    "title":title,
    "body":body
  }
  try:
    response = requests.put(f"{BASE_URL}/{id}",json=data)
    response.raise_for_status()
    return response.status_code
  except requests.exceptions.ConnectTimeout:
    print("Running timeout!")
    return None
  except requests.exceptions.ConnectionError:
    print("No internet connection!")
    return None
  except requests.exceptions.HTTPError as e:
    print("HTTP_ERROR:",e)
    return None
  except requests.exceptions.RequestException as e:
    print("Something went wrong: ",e)
    return None
  
def delete_post(id):
  try:
    response = requests.delete(f"{BASE_URL}/{id}")
    response.raise_for_status()
    return response.status_code
  except requests.exceptions.ConnectTimeout:
    print("Running timeout!")
    return None
  except requests.exceptions.ConnectionError:
    print("No internet connection!")
    return None
  except requests.exceptions.HTTPError as e:
    print("HTTP_ERROR:",e)
    return None
  except requests.exceptions.RequestException as e:
    print("Something went wrong: ",e)
    return None
while True:  
  print("==="*30)
  print("   "*12 ,"POST MANAGER")
  print("==="*30)
  print("1. View all posts 2. View post using ID")
  print("3. Create new post 4. Update post")
  print("5. Delete post 6.Exit")
  try:
    option = int(input("Enter your choice : "))
    if option == 1:
      data = show_all_posts()
      print(data)
    elif option == 2:
      try:
        id = int(input("Enter id to find post: "))
        data = single_post(id)
        print(data)
      except ValueError:
        print("Enter number only!")
    elif option == 3:
      try:
        user_id = int(input("Enter user id: "))
        id = int(input("Enter id: "))
        title = input("Enter title: ")
        body = input("Enter body: ")
        data = create_new_post(user_id,id,title,body)   
        if data["status"] == 201:
          print("Post created successfully")
          print(data["data"])
      except ValueError as e:
        print("Error:",e)
    elif option == 4:
      try:
        id = int(input("enter id who you want to update: "))
        title = input("Enter updated title: ")
        body = input("Enter updated body: ")
        data = update_post(id,title,body)
        if data == 200:
          print("post updated successfully!")
      except ValueError as e:
        print("ERROR: ",e)
    elif option == 5:
      try:
        id = int(input("Enter id for delete post: "))
        data = delete_post(id)
        if data == 200:
          print("Post deleted sucessfully!")
      except ValueError as e:
        print("ERROR: ",e)
    elif option == 6:
      break
    else:
      print("Invalid option, Please try again.")
  except ValueError:
    print("Option should be in number!")