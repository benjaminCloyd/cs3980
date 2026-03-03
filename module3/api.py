from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/hi")
async def welcome1() -> dict:
    return {"message": "hi World"}
