from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Record:
    external_id: str
    amount: Decimal
    currency: str


class DifferenceVisitor(Protocol[T]):
    def visit_missing(self, difference: "MissingRecord") -> T: ...
    def visit_mismatch(self, difference: "RecordMismatch") -> T: ...


class Difference(Protocol):
    external_id: str

    def accept(self, visitor: DifferenceVisitor[T]) -> T: ...


@dataclass(frozen=True)
class MissingRecord:
    external_id: str
    missing_side: str
    existing: Record

    def accept(self, visitor: DifferenceVisitor[T]) -> T:
        return visitor.visit_missing(self)


@dataclass(frozen=True)
class RecordMismatch:
    external_id: str
    reason: str
    left: Record
    right: Record

    def accept(self, visitor: DifferenceVisitor[T]) -> T:
        return visitor.visit_mismatch(self)
