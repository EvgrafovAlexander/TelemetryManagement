# stdlib
import uuid
from datetime import datetime

# thirdparty
from sqlalchemy import between, select, desc

# project
from src.management.models import Telemetry
from src.management.schemas import TelemetryRow
from src.utils.repository import BaseRepository


class TelemetryRepository(BaseRepository):
    model = Telemetry

    async def get_last_telemetry_row(self, device_id: uuid.UUID) -> Telemetry | None:
        query: str = (
            select(self.model)
            .filter(self.model.device_id == str(device_id))
            .order_by(desc(Telemetry.timestamp))
            .limit(1)
        )
        telemetry_raw = await self.session.execute(query)
        telemetry_row = telemetry_raw.scalar_one_or_none()
        return telemetry_row

    async def get_history_telemetry_rows(self, device_id: uuid.UUID, dt_from: datetime, dt_to: datetime) -> list[Telemetry]:
        query: str = (
            select(self.model)
            .where(
                self.model.device_id == str(device_id),
                between(Telemetry.timestamp, dt_from, dt_to)
            )
        )
        telemetry_raw = await self.session.execute(query)
        telemetry_rows = telemetry_raw.scalars().all()
        return telemetry_rows

    async def save_telemetry_row(self, telemetry_row: TelemetryRow):
        telemetry_model = self.model(
            id=telemetry_row.id,
            device_id=telemetry_row.device_id,
            value=telemetry_row.value,
            timestamp=telemetry_row.timestamp,
        )
        self.session.add(telemetry_model)
        await self.session.commit()
