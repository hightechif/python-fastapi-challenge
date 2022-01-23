# Import dependencies
from app.dependencies import *
from fastapi import APIRouter
from fastapi_pagination import Page, add_pagination, paginate
from app.database import db # DB config
from app.models.User import User
from app.dto.UserDTO import UserDTO

router = APIRouter()

# Fetch All Users
@router.get("", response_model=Page[User])
async def fetch_users():
    return paginate(db)

add_pagination(router)

# Fetch User by Id
@router.get("/{user_id}")
async def fetch_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} doesn't exist."
    )

# Create New User
@router.post("/create")
async def register_user(user: User):
    db.append(user)
    return {"message": "New user successfully created", "id": user.id}

# Delete a User
@router.delete("/delete/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User successfully deleted", "id": user.id}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} doesn't exist."
    )

#  Update a user
@router.put("/update/{user_id}")
async def update_user(user_id: UUID, userDTO: UserDTO):
    for user in db:
        if user.id == user_id:
            if userDTO.first_name is not None:
                user.first_name = userDTO.first_name
            if userDTO.last_name is not None:
                user.last_name = userDTO.last_name
            if userDTO.middle_name is not None:
                user.middle_name = userDTO.middle_name
            if userDTO.roles is not None:
                user.roles = userDTO.roles
            return {"message": "User successfully updated", "id": user.id}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} doesn't exist."
    )
