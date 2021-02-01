from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class HealthStatusEnum(str, Enum):
    UP = "healthy"
    DOWN = "unhealthy"


class ComponentHealth(BaseModel):
    name: str
    status: HealthStatusEnum
    error: Optional[str] = None


class HealthResponse(BaseModel):
    name: str
    status: HealthStatusEnum
    components: List[ComponentHealth]
