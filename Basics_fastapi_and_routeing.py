from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main_page(coding='utf-8'):
    return ('Main page')


@app.get('/user/admin')
async def admin_page():
    return ('You are logged in as an administrator')


@app.get('/user/{user_id}')
async def user_id(user_id: int):
    return (f'You are logged in as a user number {user_id}')


@app.get('/user')
async def new_user(username: str, age: int):
    return (f'User information. Name: {username}, Age: {age}')
