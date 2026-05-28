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
@app.get("/custom_headers/")
async def custom_header():
    headers={"X-Custom-Header":"MyCustomValue"}
    return JSONResponse(content={"massage":"Custom headers added"}, headers=headers)
@app.get("/stu/{stu_id}")
async def read_stu(stu_id:str):
    if stu_id not in database:
        raise HTTPException(
            status_code=404,
            detail="Student Not found"
        )
    return database[stu_id]
"""Practice sinchronus and Asynchonus"""
import asyncio
async def fake_db_query():
    await asyncio.sleep(2)
    return {"massage":"Database query completed"}
@app.get("/async-example")
async def async_example():
    result=await fake_db_query()
    return result