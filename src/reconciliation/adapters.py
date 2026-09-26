import csv
from decimal import Decimal
from pathlib import Path
from typing import Iterable
from .domain import Record


class CsvRecordSource:
    def __init__(self, path: Path) -> None:
        self._path = path

    def records(self) -> Iterable[Record]:
        with self._path.open(newline="", encoding="utf-8") as stream:
            for row in csv.DictReader(stream):
                yield Record(row["external_id"], Decimal(row["amount"]), row["currency"])


class InMemoryRecordSource:
    def __init__(self, records: Iterable[Record]) -> None:
        self._records = tuple(records)

    def records(self) -> Iterable[Record]:
        return self._records
