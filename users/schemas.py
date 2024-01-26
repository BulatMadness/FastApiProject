from typing import Annotated

from annotated_types import MinLen
from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3)]
    email: EmailStr


