from typing import Union

from pydantic import BaseModel, Field

from models import RoleEnum, StatusEnum


class UserIn(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    password: str
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[RoleEnum] = []
    status: StatusEnum = StatusEnum.active


class UserInDB(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    hashed_password: str
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[RoleEnum] = []
    status: StatusEnum = StatusEnum.active


class UserOut(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[RoleEnum] = []
    status: str = StatusEnum.active
