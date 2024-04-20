from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class NotifyTypeEnum(str, Enum):
    transaction = "transaction"
    verify_email = "verify-email"


class Notification(BaseModel):
    notify_type: NotifyTypeEnum = Field(...)
    notify_senderId: int
    notify_receivedId: int
    notify_content: str
    notify_options: Any
