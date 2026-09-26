from .domain import Difference, MissingRecord, RecordMismatch
from .ports import MatchingPolicy, RecordSource


class ReconcileRecords:
    def __init__(self, policy: MatchingPolicy) -> None:
        self._policy = policy

    def execute(
        self, left_source: RecordSource, right_source: RecordSource
    ) -> list[Difference]:
        left = {record.external_id: record for record in left_source.records()}
        right = {record.external_id: record for record in right_source.records()}
        differences: list[Difference] = []
        for key in sorted(left.keys() | right.keys()):
            if key not in left:
                differences.append(MissingRecord(key, "left", right[key]))
            elif key not in right:
                differences.append(MissingRecord(key, "right", left[key]))
            elif reason := self._policy.mismatch_reason(left[key], right[key]):
                differences.append(RecordMismatch(key, reason, left[key], right[key]))
        return differences
