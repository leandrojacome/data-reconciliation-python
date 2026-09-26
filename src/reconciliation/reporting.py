from dataclasses import dataclass, field
from .domain import DifferenceVisitor, MissingRecord, RecordMismatch


@dataclass
class SummaryVisitor(DifferenceVisitor[None]):
    counts: dict[str, int] = field(default_factory=dict)

    def _increment(self, reason: str) -> None:
        self.counts[reason] = self.counts.get(reason, 0) + 1

    def visit_missing(self, difference: MissingRecord) -> None:
        self._increment(f"missing_{difference.missing_side}")

    def visit_mismatch(self, difference: RecordMismatch) -> None:
        self._increment(difference.reason)

    def summarize(self, differences: list[MissingRecord | RecordMismatch]) -> dict[str, int]:
        for difference in differences:
            difference.accept(self)
        return dict(sorted(self.counts.items()))
