from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

from fastapi.responses import PlainTextResponse
from todo_routes import todo_router

app = FastAPI(
    title="Todo Items App",
    summary="This is a todo list app",
    description="""
    # Heading 1
    ## Heading 2
""",
    version="1.2.0",
    terms_of_service="MIT",
    contact={"name": "ben", "email": "nooooo"},
)


@app.get("/items/{item_id}")
async def get_item_by_id(
    item_id: Annotated[int, Path(gt=0, le=1000, multiple_of=3)],
) -> dict:
    return {"item_id": item_id}


app.include_router(todo_router, tags=["Todos"], prefix="/todos")


@app.exception_handler(HTTPException)
async def my_http_exception_handler(request, ex):
    return PlainTextResponse(str(ex.detail), status_code=ex.status_code)
