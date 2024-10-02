# thirdparty
from fastapi import FastAPI


def get_fastapi_application() -> FastAPI:
    application = FastAPI()
    initialize_middlewares(application)
    initialize_routers(application)

    return application


def initialize_routers(application: FastAPI):
    from src.router_initializer import get_routers

    for router in get_routers():
        application.include_router(router)


def initialize_middlewares(application: FastAPI) -> FastAPI:
    return application
