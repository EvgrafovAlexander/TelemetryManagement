# stdlib
import uuid

# thirdparty
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.database import get_db_session

router = APIRouter(tags=["telemetry"])


@router.get("/devices/{device_id}/telemetry/latest")
async def get_last_telemetry_value(
    device_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
):
    """Получает последние данные телеметрии устройства по его ID"""
    return None  # await GetDeviceInfoController(device_id, session)()


@router.get("/devices/{device_id}/telemetry")
async def get_history_telemetry_value(
    device_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
):
    """Получает исторические данные телеметрии устройства по его ID"""
    return None  # await GetDeviceInfoController(device_id, session)()


@router.post("/telemetry")
async def save_telemetry(
    # telemetry_data: TelemetryData,
    session: AsyncSession = Depends(get_db_session),
):
    """Сохраняет данные телеметрии, ранее полученные монолитом"""
    return None  # await GetDeviceInfoController(device_id, session)()
