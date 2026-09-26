# Explainable Data Reconciliation

An explainable engine that reconciles records from two sources and classifies missing records and mismatches. It is useful for migrations, financial integrations, and data-pipeline validation.

## Architecture and patterns

- **Strategy:** exact and tolerance-based policies vary without changing the use case.
- **Adapter:** CSV and memory implement the same input port.
- **Visitor:** typed discrepancies produce summaries without presentation conditionals inside entities.
- **SOLID/Clean Architecture:** domain and application do not depend on files, frameworks, or databases.
- **Pragmatic DDD:** the Record Reconciliation bounded context uses explicit language and typed discrepancies to preserve domain meaning.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
```

See [Architecture](docs/architecture.md) and [ADR-001](docs/adr/001-decimal-and-policy.md).

## Trade-offs

In-memory indexing keeps the implementation clear and O(n), but it is unsuitable for datasets larger than available memory. A production adapter could perform a streaming merge-sort or delegate the join to a database.

Visitor fits because new projections such as summaries, audit exports, and alerts are more likely than new discrepancy types. Scattered `isinstance` checks and generic dictionaries were rejected because they lose type information and distribute decisions.

## License

MIT
