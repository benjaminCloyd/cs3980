from fastapi import FastAPI, Response, status, APIRouter
from tesla_models import TeslaModel


app = FastAPI()

router = APIRouter(prefix="/tesla", tags=["Tesla"])
items_router = APIRouter(prefix="/items", tags=["Items"])


@app.get("/")
async def welcome() -> dict:
    return {"message": "hello"}


@items_router.get("/")
async def get_items() -> list[str]:
    return ["item1", "item2"]


@items_router.get("/{id}")
async def get_item_by_id(id: int, response: Response) -> dict:
    if id == 1:
        return {"id": 1, "name": "item1"}
    if id == 2:
        return {"id": 2, "name": "item2"}
    response.status_code = status.HTTP_204_NO_CONTENT
    return {"message": "no content"}


@app.get("/users/me")
async def get_me() -> str:
    return "me"


@app.get("/users/me")
async def get_me2() -> str:
    return "me2"


@app.get("/users/{id}")
async def get_by_id(id) -> str:
    return id


@items_router.post("/")
async def add_new_item(new_item: str) -> list[str]:
    items = ["item1", "item2"]
    items.append(new_item)
    return items


@router.get("/{name}")
async def get_tesla_model(name: TeslaModel) -> str:
    if name is TeslaModel.model_x:
        return "price: 2000"
    if name is TeslaModel.model_s:
        return "Model S: $30,000"
    return f"Model {name}, too expensive for u"


app.include_router(router)
app.include_router(items_router)
