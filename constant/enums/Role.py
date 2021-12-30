from enum import Enum

# Role Enum Class
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"