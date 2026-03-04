import json
from pathlib import Path
from typing import List

from fastapi import APIRouter, HTTPException
from schema import User, UserCreate

router = APIRouter()

DATA_FILE = Path(__file__).resolve().parent.parent / "users.txt"


def read_users() -> List[dict]:
    if not DATA_FILE.exists():
        return []
    raw = DATA_FILE.read_text().strip()
    if not raw:
        return []
    try:
        data = json.loads(raw)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def write_users(users: List[dict]) -> None:
    DATA_FILE.write_text(json.dumps(users, indent=2))


def next_id(users: List[dict]) -> int:
    return max((u.get("id", 0) for u in users), default=0) + 1


@router.post("/", response_model=User, status_code=201)
def create_user(payload: UserCreate):
    users = read_users()
    new_user = {"id": next_id(users), "name": payload.name, "email": payload.email}
    users.append(new_user)
    write_users(users)
    return new_user


@router.get("/", response_model=List[User])
def get_all_users():
    return read_users()


@router.get("/search", response_model=List[User])
def search_users(q: str):
    users = read_users()
    ql = q.lower()
    return [u for u in users if ql in u["name"].lower()]


@router.get("/{id}", response_model=User)
def get_user_by_id(id: int):
    users = read_users()
    user = next((u for u in users if u["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{id}", response_model=User)
def update_user(id: int, payload: UserCreate):
    users = read_users()
    for u in users:
        if u["id"] == id:
            u["name"] = payload.name
            u["email"] = payload.email
            write_users(users)
            return u
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    new_users = [u for u in users if u["id"] != id]
    if len(new_users) == len(users):
        raise HTTPException(status_code=404, detail="User not found")
    write_users(new_users)
    return {"message": "User deleted", "id": id}
