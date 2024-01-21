from datetime import datetime
from enum import Enum
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

mock_users = [
    {"id": 1, "name": "Bob", "role": "user"},
    {"id": 2, "name": "Jack", "role": "user"},
    {
        "id": 3,
        "name": "Homer",
        "role": "admin",
        "degree": [
            {
                "id": 1,
                "created_at": "2024-01-21T21:36:00.597Z",
                "type_of_degree": "expert",
            }
        ],
    },
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_of_degree: DegreeType


class User(BaseModel):
    id: int
    name: str
    role: str
    degree: List[Degree] | str = "Роль не выдана"


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in mock_users if user.get("id") == user_id]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(
        filter(lambda user: user.get("id") == user_id, mock_users)
    )[0]
    current_user["name"] = new_name
    return {"status": "200", "data": current_user}


mock_games = [
    {"id": 1, "title": "GTA V", "price": 2500},
    {"id": 2, "title": "PUBG", "price": 1000},
    {"id": 3, "title": "CS-2", "price": 350},
]


@app.get("/games")
def get_games():
    return mock_games


class Game(BaseModel):
    id: int
    title: str = Field(max_length=15)
    price: float = Field(ge=0)


@app.post("/games")
def add_game(games: List[Game]):
    mock_games.extend(games)
    return {"status": "200", "data": mock_games}
