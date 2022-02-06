# Import modules
from typing import Optional, List

from pydantic import BaseModel

from app.constants import Role, Gender, Category


# Course Schema Class
class CourseBase(BaseModel):
    name: str
    category: List[Category] = []


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# User Schema Class
class UserBase(BaseModel):
    username: str
    email: str
    fullname: str
    gender: Optional[Gender] = None
    roles: Optional[List[Role]] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
