from sqlalchemy.orm import Session

from app import models, schemas
from app.constants import Role


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        username=user.username,
        email=user.email,
        fullname=user.fullname,
        hashed_password=fake_hashed_password,
        gender=user.gender,
        roles=[Role.USER]
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_course(db: Session, course: schemas.CourseCreate, user_id: int):
    db_course = models.Course(**course.dict(), owner_id=user_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()
