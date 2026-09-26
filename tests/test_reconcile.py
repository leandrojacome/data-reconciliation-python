from decimal import Decimal

from reconciliation.adapters import InMemoryRecordSource
from reconciliation.domain import Record
from reconciliation.policies import AmountTolerancePolicy, ExactPolicy
from reconciliation.reporting import SummaryVisitor
from reconciliation.use_case import ReconcileRecords


def source(*records: Record) -> InMemoryRecordSource:
    return InMemoryRecordSource(records)


def test_reports_missing_and_changed_records() -> None:
    left = source(Record("a", Decimal(10), "BRL"), Record("b", Decimal(5), "BRL"))
    right = source(Record("a", Decimal(11), "BRL"), Record("c", Decimal(8), "BRL"))
    result = ReconcileRecords(ExactPolicy()).execute(left, right)
    assert [item.external_id for item in result] == ["a", "b", "c"]
    assert SummaryVisitor().summarize(result) == {
        "amount_mismatch": 1,
        "missing_left": 1,
        "missing_right": 1,
    }


def test_tolerance_policy_accepts_small_rounding_difference() -> None:
    left = source(Record("a", Decimal("10.00"), "BRL"))
    right = source(Record("a", Decimal("10.01"), "BRL"))
    assert (
        ReconcileRecords(AmountTolerancePolicy(Decimal("0.01"))).execute(left, right)
        == []
    )


def test_visitor_adds_a_new_projection_without_changing_difference_types() -> None:
    left = source(Record("a", Decimal(10), "BRL"))
    right = source(Record("a", Decimal(11), "BRL"), Record("b", Decimal(5), "BRL"))
    differences = ReconcileRecords(ExactPolicy()).execute(left, right)
    assert SummaryVisitor().summarize(differences) == {
        "amount_mismatch": 1,
        "missing_left": 1,
    }
