# Import dependencies
from dependencies import *
from fastapi import APIRouter
from models.User import User
from config.db import db # DB config
from dto.UserDTO import UserDTO

user_router = APIRouter()
