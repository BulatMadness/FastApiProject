from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def list_items():
    return ["Item1", "Item2", "Item3"]


@router.get("/latest")
def get_latest_item():
    return {"data": {"id": 0, "title": "Latest item"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {"item": {"id": item_id}}
