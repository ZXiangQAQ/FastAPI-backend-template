import time
from fastapi import FastAPI
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

from core.config import DEBUG, VERSION, PROJECT_NAME, ALLOWED_HOSTS, API_PREFIX
from api.routers import router as api_router
from db.session import SessionLocal as Session


def get_applications() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_router, prefix=API_PREFIX)
    return application


app = get_applications()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
