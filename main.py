from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

users = [{"first_name": "Binh", "last_name": "Nguyen", "age": 18}]

@app.get("/", description="Hello world api")
async def root():
    return {"message": "Hello world"}

@app.get("/users")
async def get_users(page: int = 0, limit: int = 10, sort: Union[str, None] = None):
    return {"message": "Hello world"}

@app.get("/users/{id}")
async def get_user(id: int):
    return {"message": "Hello world" + " " + id}

@app.get("/users/me")
async def get_current_user():
    return {"message": "Hello world"}

@app.post("/")
def post():
    return {"message": "Post api" }

@app.put("/users/{id}")
async def update_user(id: int, user: User):
    return {"id": id, "user": {"first_name": user.first_name, "last_name": "Nguyen", "age": 18}, "message": "Hello world"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
    return {"food_name": food_name}



users = [{}]
