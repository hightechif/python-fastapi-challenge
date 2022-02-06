# Import dependencies
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.database import get_db

router = APIRouter()


# Fetch All Users
@router.get("", response_model=Page[schemas.User])
async def fetch_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = crud.get_users(db, skip, limit)
    return paginate(users)


add_pagination(router)


# Fetch User by Id
@router.get("/{user_id}")
async def fetch_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} doesn't exist."
    )


# Create New User
@router.post("/create", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


# Create New Course
@router.post("/{user_id}/create-course", response_model=schemas.Course, status_code=status.HTTP_201_CREATED)
async def create_course(course: schemas.CourseCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_user_course(db, course, user_id)

# # Delete a User
# @router.delete("/delete/{user_id}")
# async def delete_user(user_id: int):
#     users = db.session.query(models.User).all()
#     for user in users:
#         if user.id == user_id:
#             db.session.query(models.User).delete()
#             return {"message": "User successfully deleted", "id": user.id}
#     raise HTTPException(
#         status_code=404,
#         detail=f"user with id: {user_id} doesn't exist."
#     )
#
#
# #  Update a user
# @router.put("/update/{user_id}")
# async def update_user(user_id: int, userDTO: UserDTO):
#     users = db.session.query(UserModel).all()
#     for user in users:
#         if user.id == user_id:
#             if userDTO.first_name is not None:
#                 user.first_name = userDTO.first_name
#             if userDTO.last_name is not None:
#                 user.last_name = userDTO.last_name
#             if userDTO.middle_name is not None:
#                 user.middle_name = userDTO.middle_name
#             if userDTO.roles is not None:
#                 user.roles = userDTO.roles
#             return {"message": "User successfully updated", "id": user.id}
#     raise HTTPException(
#         status_code=404,
#         detail=f"user with id: {user_id} doesn't exist."
#     )
