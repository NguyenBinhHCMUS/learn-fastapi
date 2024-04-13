from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Union
from pydantic import BaseModel, Field

app = FastAPI()


class Image(BaseModel):
    url: str = Field(...,
                     pattern="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)")
    name: str
    type: str
    size: float


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone_number: Union[str, None] = None


class Profile(BaseModel):
    address: str
    description: Union[str, None] = Field(None, title="The description of the profile", max_length=256)
    age: int = Field(..., gt=0, description="The age must be greater than zero.")
    tax: Union[float, None] = None
    hobbies: list[str] = []
    avatar: Union[Image, None] = None


users = [{"first_name": "Binh", "last_name": "Nguyen", "age": 18}]


@app.get("/", description="Hello world api")
async def root():
    return {"message": "Hello world"}


@app.get("/users")
async def get_users(keyword: str = Query(None, min_length=0, max_length=256, title="Search by keyword"),
                    page: int = 0,
                    limit: int = 10, sort: Union[str, None] = None
                    ):
    return {"message": "Hello world"}


@app.get("/users/{id}")
async def get_user(id: int = Path(..., title="The ID of the user to get", ge=1, le=100)):
    return {"message": "Hello world" + " "}


@app.get("/users/me")
async def get_current_user():
    return {"message": "Hello world"}


@app.post("/users")
def create_user(user: User):
    user_dict = user.dict()
    if user.phone_number:
        phone_number_with_prefix = "(+84)" + user.phone_number[1:]
        user_dict.update({"phone_number_with_prefix": phone_number_with_prefix})
    return user_dict


@app.put("/users/{id}")
async def update_user(*, id: int = Path(..., title="The ID the user to update"), user: User,
                      profile: Profile = Body(..., embed=True)):
    return {"id": id, "user": {"first_name": user.first_name, **user.dict()}, "message": "Hello world"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
    return {"food_name": food_name}


users = [{}]
