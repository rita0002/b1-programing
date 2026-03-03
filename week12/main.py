from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


class User(BaseModel):
    id: int
    name: str
    age: int

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if not os.path.exists("users.txt"):
        return {"message": "No users found."}
    with open("users.txt", "r") as f:
        users = [json.loads(line) for line in f]
    for user in users:
        if user.get("id") == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User):
    with open("users.txt", "a") as f:
        f.write(user.model_dump_json() + "\n")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if not os.path.exists("users.txt"):
        raise HTTPException(status_code=404, detail="No users to delete")
    with open("users.txt", "r") as f:
        users = [json.loads(line) for line in f]
    new_users = [user for user in users if user.get("id") != user_id]
    if len(new_users) == len(users):
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    with open("users.txt", "w") as f:
        for user in new_users:
            f.write(json.dumps(user) + "\n")
    return {"message": f"User {user_id} deleted"}