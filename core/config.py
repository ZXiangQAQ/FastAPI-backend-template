from typing import List

from pydantic import AnyUrl

# https://www.starlette.io/config/
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

API_PREFIX = "/api"
VERSION = "0.0.0"

# Config will be read from environment variables and/or ".env" files.
config = Config(".env")

ENV: str = config("ENV", cast=str, default="dev")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
PROJECT_NAME: str = config("PROJECT_NAME", default="Joker Private Cloud Manager")
ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="")


# Database config
class DatabaseDSN(AnyUrl):
    user_required = True
    allowed_schemes = {'mysql', 'sqlite'}
    # driver: Optional[str] = "mysqlclient"


DATABASE_TYPE: str = config("DATABASE_TYPE", default="mysql")
DATABASE_SERVER: str = config("MySQL_SERVER", default="192.168.1.247")
DATABASE_USER: str = config("MySQL_USER", default="root")
DATABASE_PORT: str = config("DATABASE_PORT", default="13306")
DATABASE_PASSWORD: str = config("MySQL_PASSWORD", default="123456")
DATABASE_DB: str = config("MySQL_DB", default="joker_v4")

DATABASE_URL: str = DatabaseDSN.build(
    scheme=DATABASE_TYPE,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    port=DATABASE_PORT,
    host=DATABASE_SERVER,
    path=f"/{DATABASE_DB}"
)

# Pagination config
DEFAULT_PAGE_NUM: int = 0
DEFAULT_PAGE_SIZE: int = 20

# auth key
OPS_NXP_TOKEN: str = "63c971cf04da43a66a27e33b210de5d30ecdcd99"
