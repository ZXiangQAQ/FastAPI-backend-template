from fastapi import APIRouter

from api.v1.sys_health import router as health

"""
    总路由入口
"""
router = APIRouter()

router.include_router(health, tags=["health"], prefix="/health")
