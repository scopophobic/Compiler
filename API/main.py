from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}



@app.get("/user/me")
async def read_user_me(user_id:str):
    return {"user_id":"the current user"}