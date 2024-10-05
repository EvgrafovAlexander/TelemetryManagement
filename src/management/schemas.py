# stdlib
from datetime import datetime
from uuid import UUID

# thirdparty
from pydantic import BaseModel, Field


class TelemetryRow(BaseModel):
    """Запись со значением телеметрии датчика"""

    id: UUID = Field(default_factory=UUID, title="Row id")
    device_id: UUID = Field(title="Device id")
    value: int | float = Field(title="Value")
    timestamp: datetime = Field(title="Timestamp")


class Result(BaseModel):
    """Модель результата успешного выполнения запроса"""

    success: bool = Field(title="True/False")
