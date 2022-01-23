from app.dependencies import *

# Role Enum Class
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    STUDENT = "student"