from typing import Union
from pydantic import BaseModel, Field, EmailStr

from models import RoleEnum, StatusEnum


class User(BaseModel):
    user_name: str = Field(..., max_length=64, example="binhbong")
    password: str
    first_name: str
    last_name: str
    phone_number: Union[str, None] = None
    roles: list[RoleEnum] = []
    status: StatusEnum = StatusEnum.active

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
