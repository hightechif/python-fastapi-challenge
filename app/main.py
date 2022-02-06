# Import modules
# import uvicorn
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import api_router

from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

# App instantiation
app = FastAPI()


# Setup CORS Origins
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Simple asynchronous GET Request
@app.get("/")
async def read_root():
    return {
        "hello": "fadhil"
    }


# Simple asynchronous GET Request with Path variable and Query parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


app.include_router(api_router, prefix="/api/v1")

# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)
