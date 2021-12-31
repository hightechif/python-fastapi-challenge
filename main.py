# Import modules
from dependencies import *
from core.database import db # DB config
from core.models.User import User
from core.dto.UserDTO import UserDTO
from routes.users import user_router

# App instantiation
app = FastAPI()

# Simple asynchronous GET Request
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Simple asynchronous GET Request with Path variable and Query parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# Fetch All Users
@app.get("/api/v1/users")
async def fetch_users():
    return db

# Fetch User by Id
@app.get("/api/v1/users/{user_id}")
async def fetch_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} doesn't exist."
    )

# Create New User
@app.post("/api/v1/users/create")
async def register_user(user: User):
    db.append(user)
    return {"message": "New user successfully created", "id": user.id}

# Delete a User
@app.delete("/api/v1/users/delete/{user_id}")
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
@app.put("/api/v1/users/update/{user_id}")
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

