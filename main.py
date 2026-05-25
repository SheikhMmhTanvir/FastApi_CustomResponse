from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()
class User(BaseModel):
    Name:str
    ID: str
database=[{"Name":"Tanvir","ID":"C231306", "Pass":"1234"}]
@app.get("/user")
async def user_info():
    responseData={
        "Name":database[0]["Name"],
        "ID": database[0]["ID"]
    }
    return JSONResponse(content=responseData)

@app.get("/userInfo", response_model=list[User])
async def user_info():
    return database
