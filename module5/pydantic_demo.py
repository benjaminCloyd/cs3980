from pydantic import BaseModel, PositiveInt, ValidationError
from datetime import datetime


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_timestamp: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    "id": 123,
    "name": "Tom",
    "signup_timestamp": "2026-02-19 12:57",
    "tastes": {"beer": 10, "cabbage": 5},
}
try:
    user = User(**external_data)
    print(user.id)
    print(user.name)
    print(user.signup_timestamp)
    print(user.tastes)
except ValidationError as e:
    print(e.errors())
