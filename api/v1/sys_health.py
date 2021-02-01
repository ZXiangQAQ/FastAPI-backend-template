from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.dependencies.db import get_db_session
from core.config import PROJECT_NAME
from schema.response.sys_health import HealthResponse, HealthStatusEnum
from service.sys_health import get_database_health


router = APIRouter()


@router.get("/", response_model=HealthResponse, response_model_exclude_unset=True)
async def health_handle(db: Session = Depends(get_db_session)) -> HealthResponse:
    components = [get_database_health(db), ]
    response = HealthResponse(name=PROJECT_NAME, status=HealthStatusEnum.UP, components=components)
    for c in components:
        if c.status == HealthStatusEnum.DOWN:
            response.status = HealthStatusEnum.DOWN
            break
    return response
