from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from models import User

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/sum")
async def sum(request: Request):
    num1 = await request.form['number1']
    num2 = await request.form['number2']
    return {'result': int(num1) + int(num2)}

@app.get("/custom")
async def read_custom_message():
    return {"message":  "This is a cutom message!"}

@app.get("/get_user")
async def get_user():
    return my_user

@app.post("/post_user")
async def adult_user(user: User):
    return {"name": user.name,
            "age": user.age,
            "is_adult": user.age >= 18
            }

my_user = {"id": 1, "name": "Elon Musk", "age": 45}


