# Import modules
from app.dependencies import *
from app.database import db # DB config
from app.models.User import User
from app.dto.UserDTO import UserDTO
from app.api.api import api_router
# from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

# App instantiation
app = FastAPI(
    # title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

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
    return {"Hello": "World"}

# Simple asynchronous GET Request with Path variable and Query parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

app.include_router(api_router, prefix="/api/v1")
