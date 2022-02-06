from fastapi import APIRouter

from app.api.endpoints import user_controller, course_controller

api_router = APIRouter()
api_router.include_router(user_controller.router, prefix="/users", tags=["users"])
api_router.include_router(course_controller.router, prefix="/courses", tags=["courses"])
