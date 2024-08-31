from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
def user_reg(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
def user_put(user_id: int, user: User) -> User:
    try:
        for index, existing_user in enumerate(users):
            if existing_user.id == user_id:
                users[index].username = user.username
                users[index].age = user.age
                return users[index]
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
def delete_user(user_id: int) -> User:
    try:
        for index, existing_user in enumerate(users):
            if existing_user.id == user_id:
                return users.pop(index)
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
