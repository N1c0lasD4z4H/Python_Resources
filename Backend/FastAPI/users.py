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
    


def search_user(id: int):
    users= filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error": "No se ha encontrado el usuario"}