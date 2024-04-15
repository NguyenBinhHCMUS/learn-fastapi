from pydantic import BaseModel, Field


class ImageCustom(BaseModel):
    url: str = Field(...,
                     pattern="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)")
    name: str
    type: str
    size: float
