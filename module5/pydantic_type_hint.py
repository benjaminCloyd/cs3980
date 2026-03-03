from annotated_types import Gt
from pydantic import BaseModel
from typing import Literal, Annotated


class Fruit(BaseModel):
    name: str
    color: Literal["red", "green", "orange"]
    weight: Annotated[float, Gt(0)]


f = Fruit(name="Apple", color="red", weight=110.2)
f = Fruit("Apple", "green", 98.5)
