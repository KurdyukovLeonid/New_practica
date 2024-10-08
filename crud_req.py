from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Name: Example, age: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def user_reg(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Name: {username}, age: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def user_put(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'
