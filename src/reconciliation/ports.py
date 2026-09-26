from typing import Iterable, Protocol
from .domain import Record


class RecordSource(Protocol):
    def records(self) -> Iterable[Record]: ...


class MatchingPolicy(Protocol):
    def mismatch_reason(self, left: Record, right: Record) -> str | None: ...
