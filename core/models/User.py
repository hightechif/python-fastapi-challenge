# Import modules
from dependencies import *
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
