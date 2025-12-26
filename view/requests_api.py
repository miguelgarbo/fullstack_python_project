import requests
from schemas import Credentials

url  = "http://127.0.0.1:8000"

def get_users(n_clicks):
    if not n_clicks:
        return 
      
    response = requests.get(f"{url}/users/")

    if response.status_code != 200:
        return "Error to fetch API"

    data = response.json()
    print(data)

    return data["users"]
    # return f"{data['name']} - {data['email']}"


def login(email, password):

  response = requests.post("http://127.0.0.1:8000/login/token",
                           data={"username": email, "password": password})
  
  
 

  print(response.status_code)
  print(response.text)

  
  if response.status_code != 200:
          return "Error to Fetch API"

  data = response.json()
  
  return data

def current_user(token:str):
  
  response = requests.get(f"{url}/current_user")

  user = response.json()
  
  return user
    

"""
{
  "users": [
    {
      "name": "string",
      "email": "user@example.com",
      "role": "ADMIN"
    }
  ]
}"""
