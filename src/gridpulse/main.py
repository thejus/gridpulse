import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/health")
async def health():
    return {"status": "OK"}


@app.get("/block")
async def block():
    time.sleep(5)
    return {"status": "OK"}


@app.get("/yield")
async def non_blocking_sleep():
    await asyncio.sleep(5)
    return {"status": "OK"}
