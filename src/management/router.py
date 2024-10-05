# stdlib
import uuid
from datetime import datetime

# thirdparty
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.database import get_db_session
from src.management.controllers.get_history_telemetry_values import GetHistoryTelemetryController
from src.management.controllers.get_last_telemetry_value import GetLastTelemetryController
from src.management.controllers.save_telemetry import SaveTelemetryController
from src.management.schemas import TelemetryRow, Result

router = APIRouter(tags=["telemetry"])


@router.get("/devices/{device_id}/telemetry/latest", response_model=TelemetryRow)
async def get_last_telemetry_value(
    device_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
):
    """Получает последние данные телеметрии устройства по его ID"""
    return await GetLastTelemetryController(device_id, session)()


@router.get("/devices/{device_id}/telemetry", response_model=list[TelemetryRow])
async def get_history_telemetry_values(
    device_id: uuid.UUID,
    dt_from: datetime,
    dt_to: datetime,
    session: AsyncSession = Depends(get_db_session),
):
    """Получает исторические данные телеметрии устройства по его ID и временному интервалу"""
    return await GetHistoryTelemetryController(device_id, dt_from, dt_to, session)()


@router.post("/telemetry", response_model=Result)
async def save_telemetry(
    telemetry_row: TelemetryRow,
    session: AsyncSession = Depends(get_db_session),
):
    """Сохраняет данные телеметрии, ранее полученные монолитом"""
    return await SaveTelemetryController(telemetry_row, session)()
