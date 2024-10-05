# stdlib
import uuid
from datetime import datetime
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.telemetry import TelemetryRepository
from src.management.schemas import TelemetryRow
from src.utils.controller import AsyncController


class GetHistoryTelemetryController(AsyncController):
    def __init__(self, device_id: uuid.UUID, dt_from: datetime, dt_to: datetime, session: AsyncSession):
        self.device_id = device_id
        self.dt_from = dt_from
        self.dt_to = dt_to
        self.session = session

    async def __call__(self, *args, **kwargs) -> list[TelemetryRow]:
        try:
            logger.info("GetHistoryTelemetryController, device_id: %s" % self.device_id)
            history_telemetry_rows = await TelemetryRepository(session=self.session).get_history_telemetry_rows(
                self.device_id, self.dt_from, self.dt_to,
            )
            if not history_telemetry_rows:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="History telemetry not found")
            return [
                TelemetryRow(
                    id=row.id,
                    device_id=row.device_id,
                    value=row.value,
                    timestamp=row.timestamp,
                )
                for row in history_telemetry_rows
            ]
        except Exception as e:
            logger.error("GetHistoryTelemetryController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"GetHistoryTelemetryController Error, detail: {e}",
            )
