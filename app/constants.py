from enum import Enum


# Gender Enum Class
class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


# Role Enum Class
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    TUTOR = "tutor"
    STUDENT = "student"


# Category Enum Class
class Category(str, Enum):
    DATA_ANALYTICS = "Data Analytics"
    DATA_SCIENCE = "Data Science"
    DATA_ENGINEERING = "Data Engineering"
