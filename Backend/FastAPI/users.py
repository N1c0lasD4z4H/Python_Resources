from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name: str
    surname: str
    age: int
    url:str

users_list = [
    User(id=1,name="Nicolas", surname="Daza", url="https://mouredev.com", age=20),
    User(id=2,name="Sam", surname="Neins", url="https://samneins.com", age=20),
    User(id=3,name="Nicol", surname="Suarez", url="https://nicol.com", age=20)
]



@app.get("/usersjson")#No es lo mas habitual
async def usersjson():
    return [{"name":"Nicolas","surname":"Daza","url":"https://mouredev.com","age":20},
            {"name":"Sam","surname":"Neins","url":"https://samneins.com","age":20},
            {"name":"Nicol","surname":"Suarez","url":"https://nicol.com","age":20}]

@app.get("/users")
async def users():
    return users_list
#Path
@app.get("/user/{ide}")
async def user(ide: int):
        return search_user(ide)
    
#Fast Api Recomienda tipar todas las variables
#Query /?id=1&name

@app.get("/userquery/")
async def user(id: int,name: str):
        return search_user(id)
    
#Put para crear nuevos datos
@app.post("/user/")
async def user(user:User):
     if type(search_user(user.id)) == User:
        return {"Error":"El usuario ya esxite"}
     else:
          users_list.append(user)
          return user

@app.put ("/user/")
async def user(user: User):
     
    found = False

    for index, save_user in enumerate(users_list):
          if save_user.id == user.id:
              users_list[index] = user
              found= True

    if not found:
        return{"Error":"No se ha actulizado el usuario"}
    else:
         return user

@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, save_user in enumerate(users_list):
        if save_user.id == id:
            del users_list[index]
            found= True
    if not found:
        return{"Error":"No se ha eliminado el usuario"}  
    
             

def search_user(id: int):
    users= filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error": "No se ha encontrado el usuario"}