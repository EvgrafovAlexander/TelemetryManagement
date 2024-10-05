# stdlib
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.telemetry import TelemetryRepository
from src.management.schemas import Result, TelemetryRow
from src.utils.controller import AsyncController


class SaveTelemetryController(AsyncController):
    def __init__(self, telemetry_row: TelemetryRow, session: AsyncSession):
        self.device_id = telemetry_row.device_id
        self.telemetry_row = telemetry_row
        self.session = session

    async def __call__(self, *args, **kwargs) -> Result:
        try:
            logger.info("SaveTelemetryController, device_id: %s" % self.device_id)
            await TelemetryRepository(session=self.session).save_telemetry_row(self.telemetry_row)
            return Result(success=True)
        except Exception as e:
            logger.error("SaveTelemetryController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"SaveTelemetryController Error, detail: {e}",
            )
