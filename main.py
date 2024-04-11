from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/", description="Hello world api")
async def root():
    return {"message": "Hello world"}

@app.get("/users")
async def get_users():
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

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
    return {"food_name": food_name}