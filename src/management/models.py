# stdlib
import uuid

# thirdparty
from sqlalchemy import Column, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID

# project
from src.database import CustomBase


class Telemetry(CustomBase):
    __tablename__ = "telemetry"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Row id"
    )
    device_id = Column(UUID(as_uuid=True))
    value = Column(Float)
    timestamp = Column(DateTime)
