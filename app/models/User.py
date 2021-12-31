# Import modules
from app.dependencies import *
from app.constant.enums.Gender import Gender
from app.constant.enums.Role import Role

# User Model Class
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str = ""
    last_name: str = ""
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
