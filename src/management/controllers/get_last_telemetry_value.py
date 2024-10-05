# stdlib
import uuid
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.telemetry import TelemetryRepository
from src.management.schemas import Result, TelemetryRow
from src.utils.controller import AsyncController


class GetLastTelemetryController(AsyncController):
    def __init__(self, device_id: uuid.UUID, session: AsyncSession):
        self.device_id = device_id
        self.session = session

    async def __call__(self, *args, **kwargs) -> TelemetryRow:
        try:
            logger.info("GetLastTelemetryController, device_id: %s" % self.device_id)
            last_telemetry_row = await TelemetryRepository(session=self.session).get_last_telemetry_row(self.device_id)
            if not last_telemetry_row:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Last telemetry not found")
            return TelemetryRow(
                id=last_telemetry_row.id,
                device_id=last_telemetry_row.device_id,
                value=last_telemetry_row.value,
                timestamp=last_telemetry_row.timestamp,
            )
        except Exception as e:
            logger.error("GetLastTelemetryController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"GetLastTelemetryController Error, detail: {e}",
            )
