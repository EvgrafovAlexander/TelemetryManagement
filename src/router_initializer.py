# thirdparty
from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.management import router as telemetry_router

    routers: list[APIRouter] = [
        telemetry_router.router,
    ]
    return routers
