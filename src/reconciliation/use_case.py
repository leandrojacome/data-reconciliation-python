from .domain import Difference
from .ports import MatchingPolicy, RecordSource


class ReconcileRecords:
    def __init__(self, policy: MatchingPolicy) -> None:
        self._policy = policy

    def execute(self, left_source: RecordSource, right_source: RecordSource) -> list[Difference]:
        left = {record.external_id: record for record in left_source.records()}
        right = {record.external_id: record for record in right_source.records()}
        differences: list[Difference] = []
        for key in sorted(left.keys() | right.keys()):
            if key not in left:
                differences.append(Difference(key, "missing_left", None, right[key]))
            elif key not in right:
                differences.append(Difference(key, "missing_right", left[key], None))
            elif reason := self._policy.mismatch_reason(left[key], right[key]):
                differences.append(Difference(key, reason, left[key], right[key]))
        return differences
