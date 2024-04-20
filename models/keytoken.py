import uuid

from pydantic import BaseModel, Field


class KeyToken(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    public_key: str = Field(...)
    private_key: str = Field(...)
    refresh_token: list[str] = Field(...)
