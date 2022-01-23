from app.dependencies import *
from app.models.User import User
from app.constant.enums.Gender import Gender
from app.constant.enums.Role import Role

# Data Seeder
db: List[User] = [
    User(
        id=UUID("e9ad1b69-bbf8-4610-a9ae-3dc63f767f4e"),
        first_name= "Jamila",
        last_name="Ahmed",
        gender=Gender.FEMALE,
        roles=[Role.STUDENT]
    ),
    User(
        id=UUID("8b24e4d3-751a-48d6-847b-b02a21c3335b"),
        first_name= "Alex",
        last_name="Jones",
        gender=Gender.MALE,
        roles=[Role.ADMIN, Role.USER]
    )
]
