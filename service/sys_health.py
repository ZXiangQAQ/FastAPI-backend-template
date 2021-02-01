from sqlalchemy.orm import Session

from schema.response.sys_health import ComponentHealth, HealthStatusEnum


def get_database_health(db: Session) -> ComponentHealth:
    result = ComponentHealth(name="database", status=HealthStatusEnum.UP)
    try:
        res = db.execute("SELECT 1")
        res.fetchall()
    except Exception as e:
        result.status = HealthStatusEnum.DOWN
        result.error = str(e.__context__)
    return result


# def get_redis_health():
#     pass
