# Import Module
from dependencies import *
from constant.enums.Role import Role

# Define User DTO Class
class UserDTO(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
