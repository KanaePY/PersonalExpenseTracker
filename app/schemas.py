from datetime import UTC, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ExpenseCreate(BaseModel):
    amount: Decimal
    category_id: int
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    note: str | None = None
    source: str | None = None


class ExpenseResponse(ExpenseCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)