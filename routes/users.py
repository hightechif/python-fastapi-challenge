# Import dependencies
from dependencies import *
from core.database import db # DB config
from core.models.User import User
from core.dto.UserDTO import UserDTO
from fastapi import APIRouter

user_router = APIRouter()
