from fastapi import FastAPI
import asyncio

app=FastAPI()

async def fetch_user_data(user_id: int):
    await asyncio.sleep(1) #API call 1 or database query
    return{"user_id": user_id, "name":"Sheikh Tanvir"}
async def fetch_transection_history(user_id:int):
    await asyncio.sleep(2) #API call 2
    return {"user_id":user_id, "transactions":["purchase1","purchase2"]}

@app.get("/user/{user_id}")
async def get_user_info(user_id:int):
    user_data=await fetch_user_data(user_id)
    transaction_data=await fetch_transection_history(user_id)
    return {**user_data, **transaction_data}
