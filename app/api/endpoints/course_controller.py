# Import dependencies
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.database import get_db

router = APIRouter()


# Fetch All Courses
@router.get("", response_model=Page[schemas.Course])
async def fetch_courses(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = crud.get_users(db, skip, limit)
    return paginate(users)


add_pagination(router)
