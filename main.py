import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def welcome_message(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {"message": "success", "email": user.email}


@app.get("/items/")
def list_items():
    return ["Item1", "Item2", "Item3"]


@app.get("/items/latest")
def get_latest_item():
    return {"data": {"id": 0, "title": "Latest item"}}


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {"item": {"id": item_id}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
