from starlette.requests import Request


def get_db_session(request: Request):
    return request.state.db
