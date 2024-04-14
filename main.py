from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from typing import Union, Annotated, Any
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, time, timedelta
from uuid import UUID

app = FastAPI()


class Image(BaseModel):
    url: str = Field(...,
                     pattern="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)")
    name: str
    type: str
    size: float


class Role(str, Enum):
    shop = "shop"
    client = "client"
    admin = "admin"
    shipper = "shipper"


class Status(str, Enum):
    active = "active"
    in_active = "in_active"
    hide = "hide"


class User(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    password: str
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[Role] = []
    status: Status = Status.active

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "user_name": "binhbong",
    #             "password": "hashpassword",
    #             "first_name": "Binh",
    #             "last_name": "Bong",
    #             "phone_number": "012345678"
    #         }
    #     }


class UserIn(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    password: str
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[Role] = []
    status: Status = Status.active


class UserOut(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[Role] = []
    status: Status = Status.active


class UserInDB(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    hashed_password: str
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[Role] = []
    status: Status = Status.active


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    print(user_in.dict())
    hashed_password = fake_password_hasher(user_in.password)
    print(hashed_password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


class Profile(BaseModel):
    email: EmailStr
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


@app.get("/users", response_model=list[User], response_model_exclude={"password"})
async def get_users(keyword: str = Query(None, min_length=0, max_length=256, title="Search by keyword"),
                    page: int = 0,
                    limit: int = 10, sort: Union[str, None] = None
                    ) -> Any:
    return [{
        "user_name": "binhbong",
        "password": "hashpassword",
        "first_name": "Binh",
        "last_name": "Bong",
        "phone_number": "012345678",
        "roles": [Role.shop],
        "status": Status.active
    }]


@app.get("/users/me", response_model=User, response_model_exclude={"password"})
async def get_current_user() -> Any:
    return {
        "id": 1,
        "user_name": "binhbong",
        "password": "hashpassword",
        "first_name": "Binh",
        "last_name": "Bong",
        "phone_number": "012345678",
        "roles": [Role.shop],
        "status": Status.active
    }


@app.get("/users/{id}")
async def get_user(id: int = Path(..., title="The ID of the user to get", ge=1, le=100)):
    return {"message": "Hello world" + " "}


@app.post("/users", response_model=UserOut)
def create_user(user: UserIn = Body(...,
                                    openapi_examples={
                                        "shop": {
                                            "user_name": "binhbong",
                                            "password": "hashpassword",
                                            "first_name": "Binh",
                                            "last_name": "Bong",
                                            "phone_number": "012345678",
                                            "roles": [Role.shop],
                                            "status": Status.active
                                        },
                                        "client": {
                                            "user_name": "binhbong",
                                            "password": "hashpassword",
                                            "first_name": "Binh",
                                            "last_name": "Bong",
                                            "phone_number": "012345678",
                                            "roles": [Role.client],
                                            "status": Status.active
                                        },
                                        "admin": {
                                            "user_name": "binhbong",
                                            "password": "hashpassword",
                                            "first_name": "Binh",
                                            "last_name": "Bong",
                                            "phone_number": "012345678",
                                            "roles": [Role.admin],
                                            "status": Status.active
                                        }
                                    })) -> Any:
    # user_dict = user.dict()
    # if user.phone_number:
    #     phone_number_with_prefix = "(+84)" + user.phone_number[1:]
    #     user_dict.update({"phone_number_with_prefix": phone_number_with_prefix})

    user_saved = fake_save_user(user)
    return user_saved


@app.put("/users/{id}")
async def update_user(*, id: int = Path(..., title="The ID the user to update"), user: User = Body(..., embed=True),
                      profile: Profile = Body(..., embed=True)):
    return {"id": id, "user": {"first_name": user.first_name, **user.dict()}, "message": "Hello world"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
    return {"food_name": food_name}


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: Annotated[Union[datetime, None], Body()] = None,
        end_datetime: Annotated[Union[datetime, None], Body()] = None,
        repeat_at: Annotated[Union[time, None], Body()] = None,
        process_after: Annotated[Union[timedelta, None], Body()] = None):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/items")
async def read_items_with_cookie(cookie_id: Annotated[Union[str, None], Cookie()] = None,
                                 accept_encoding: Annotated[Union[str, None], Header()] = None,
                                 sec_ch_ua: Annotated[Union[str, None], Header()] = None,
                                 user_agent: Annotated[Union[str, None], Header()] = None):
    return {"Cookie": cookie_id, "Accept-Encoding": accept_encoding, "Sec-Ch-Ua": sec_ch_ua,
            "User-Agent": user_agent}


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
