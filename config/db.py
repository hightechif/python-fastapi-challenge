from typing import List
from models.User import User
from constant.enums.Gender import Gender
from constant.enums.Role import Role
from uuid import UUID

db: List[User] = [
    User(
        id=UUID("e9ad1b69-bbf8-4610-a9ae-3dc63f767f4e"),
        first_name= "Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("8b24e4d3-751a-48d6-847b-b02a21c3335b"),
        first_name= "Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]
