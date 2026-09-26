# ADR-001: Decimal values and explicit matching policy

## Status

Accepted for the portfolio scope.

## Decision

Represent monetary values with `Decimal` and encapsulate tolerance in a Strategy.

## Consequences

This avoids binary floating-point errors and makes the rule auditable. Each currency may still require its own scale and rounding policy in a future evolution.
