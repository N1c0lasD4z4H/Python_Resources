from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "HEllo FastApiS"}
@app.get("/url")
async def root():
    return {"url_curso": "httpd://mouredev.com/python "}