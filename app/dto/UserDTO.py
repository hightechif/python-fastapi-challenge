# Import Module
from app.dependencies import *
from app.constant.enums.Role import Role

# Define User DTO Class
class UserDTO(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
