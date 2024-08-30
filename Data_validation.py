from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def main_page():
    return ('Main page')


@app.get('/user/admin')
async def admin_page():
    return ('You are logged in as an administrator')


@app.get('/user/{user_id}')
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    return (f'You are logged in as a user number {user_id}')


@app.get('/user/{username}/{age}')
async def new_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    return (f'User information. Name: {username}, Age: {age}')
