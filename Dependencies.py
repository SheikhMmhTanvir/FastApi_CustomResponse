from fastapi import FastAPI, Depends
from typing import Annotated

app=FastAPI()

async def commonP(q: str | None=None, skip: int=0, limit:int=10):
    return{"q":q, "skip":skip, "Limit":limit}
@app.get("/items/")
async def read_items(commons: Annotated[dict,Depends(commonP)]):
    return commons
@app.get("/user/")
async def read_user(commons: Annotated[dict, Depends(commonP)]):
    return commons