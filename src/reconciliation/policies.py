from decimal import Decimal

from .domain import Record


class ExactPolicy:
    def mismatch_reason(self, left: Record, right: Record) -> str | None:
        if left.currency != right.currency:
            return "currency_mismatch"
        if left.amount != right.amount:
            return "amount_mismatch"
        return None


class AmountTolerancePolicy:
    def __init__(self, tolerance: Decimal) -> None:
        if tolerance < 0:
            raise ValueError("tolerance must be non-negative")
        self._tolerance = tolerance

    def mismatch_reason(self, left: Record, right: Record) -> str | None:
        if left.currency != right.currency:
            return "currency_mismatch"
        if abs(left.amount - right.amount) > self._tolerance:
            return "amount_outside_tolerance"
        return None
