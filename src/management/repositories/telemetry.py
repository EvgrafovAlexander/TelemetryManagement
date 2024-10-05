# stdlib
import uuid

# thirdparty
from sqlalchemy import select, update

# project
from src.management.models import Telemetry
from src.management.schemas import TelemetryRow
from src.utils.repository import BaseRepository


class TelemetryRepository(BaseRepository):
    model = Telemetry

    async def save_telemetry_row(self, telemetry_row: TelemetryRow):
        telemetry_model = self.model(
            id=telemetry_row.id,
            device_id=telemetry_row.device_id,
            value=telemetry_row.value,
            timestamp=telemetry_row.timestamp,
        )
        self.session.add(telemetry_model)
        await self.session.commit()
