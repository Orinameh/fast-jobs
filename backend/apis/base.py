from apis.v1.blog_router import router as blog_router
from apis.v1.login_router import router as login_router
from apis.v1.user_router import router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(router, prefix="", tags=["users"])
api_router.include_router(blog_router, prefix="", tags=["blogs"])
api_router.include_router(login_router, prefix="", tags=["login"])
