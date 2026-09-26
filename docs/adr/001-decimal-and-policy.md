# ADR-001: Decimal e política explícita

## Status

Aceito.

## Decisão

Representar valores com `Decimal` e encapsular tolerância em uma Strategy.

## Consequências

Evita erros binários de ponto flutuante e torna a regra auditável. Cada moeda ainda pode exigir escala e arredondamento próprios em evolução futura.
