from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
ALGORITHM = "HS256"
# Función para buscar un usuario en la base de datos
ACCES_TOKEN_DURATION = 1
SECRET_KEY = "0a14befd6f7a468b9db6672f18ca1ce3592827620154977139c399496fe37efb"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
cript = CryptContext(schemes=["bcrypt"])

# Modelos de datos
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str



# Base de datos de usuarios (simulada)
users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "$2a$12$SpojKAWSpOChz50h9l4xtuYt8VrwGNtN6b1hs9I42VvzO/dJeYGHG"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,
        "password": "$2a$12$wiLfNHWhFp3DB160/FEFsO.Cw859QHiB.BGFt55ViQOsTzuFEy6Wq"
    },
    "NicoDaza": {
        "username": "NicoDaza",
        "full_name": "Nicolas Daza ",
        "email": "ndazah8@gmail.com",
        "disabled": True,
        "password": "$2a$12$jXL/1Ar92LgfCwFElVtmMO7EYINXZGhmK45RvIEacAvdjomVR0SrS"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username) 
     
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user

# Endpoint de login
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not -cript.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM), "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user