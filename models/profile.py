from typing import Union
from pydantic import BaseModel, EmailStr, Field

from models import ImageCustom


class Profile(BaseModel):
    email: EmailStr
    address: str
    description: Union[str, None] = Field(None, title="The description of the profile", max_length=256)
    age: int = Field(..., gt=0, description="The age must be greater than zero.")
    tax: Union[float, None] = None
    hobbies: list[str] = []
    avatar: Union[ImageCustom, None] = None
