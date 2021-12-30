# Import modules
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from constant.enums.Gender import Gender
from constant.enums.Role import Role

# User Model Class
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
