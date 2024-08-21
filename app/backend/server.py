from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: str
    token: str | None = None


app = FastAPI()

@app.post('/user/auth')
async def check_user(user: User):
    print(user.name)
    return user