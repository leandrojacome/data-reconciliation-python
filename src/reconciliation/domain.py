from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Record:
    external_id: str
    amount: Decimal
    currency: str


@dataclass(frozen=True)
class Difference:
    external_id: str
    reason: str
    left: Record | None
    right: Record | None
