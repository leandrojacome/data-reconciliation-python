# Architecture

## Domain model

The **Record Reconciliation** bounded context models `Record` as the canonical record. `Decimal` and currency compose the monetary value. `MissingRecord` and `RecordMismatch` are domain discrepancies with distinct structural invariants.

## Layers

- **Domain:** records, discrepancies, and the Visitor contract.
- **Application:** `ReconcileRecords` coordinates sources and matching policy.
- **Infrastructure:** CSV/in-memory adapters and report projections.

## Patterns and alternatives

- **Strategy:** `MatchingPolicy` varies tolerance without conditionals in the use case. A `tolerant=True` flag was rejected because it hides monetary rules.
- **Adapter:** CSV remains replaceable. Parsing inside the use case was rejected.
- **Visitor:** each discrepancy accepts independent projections such as `SummaryVisitor`. Scattered `isinstance` checks were rejected because they duplicate dispatch and violate Open/Closed when projections are added.

Visitor is appropriate because discrepancy types are few and stable while output operations are expected to grow. If types changed more often than projections, pattern matching would be simpler.
