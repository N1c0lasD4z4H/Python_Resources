from fastapi import FastAPI
from routers import products, users, basic_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static",StaticFiles(directory="static"), name="static")
app.include_router(basic_auth_users.router)

@app.get("/")
async def root():
    return {"message": "HEllo FastApieS"}
@app.get("/url")
async def root():
    return {"url_curso": "httpd://mouredev.com/python "}