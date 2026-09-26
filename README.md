# Data Reconciliation — Python

Motor explicável para reconciliar registros de duas fontes e classificar ausências ou divergências. É útil em migrações, integrações financeiras e validação de pipelines.

## Arquitetura e padrões

- **Strategy (GoF):** políticas exata e por tolerância variam sem alterar o caso de uso.
- **Adapter:** CSV e memória implementam a mesma porta de entrada.
- **Visitor (GoF):** divergências tipadas geram resumo sem condicionais ou lógica de apresentação nas entidades.
- **SOLID/Clean Architecture:** domínio e aplicação não dependem de arquivo, framework ou banco.
- **DDD proporcional:** bounded context de Reconciliação, linguagem ubíqua e divergências tipadas preservam significado de domínio.

## Executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest
pytest
pip-audit
```

Veja [Arquitetura](docs/architecture.md) e [ADR-001](docs/adr/001-decimal-and-policy.md).

## Trade-offs

A indexação em memória oferece implementação clara e O(n), mas não é adequada a datasets maiores que a memória disponível. Um adaptador de produção pode executar merge-sort por streaming ou delegar o join ao banco.

Visitor foi escolhido porque novas projeções (resumo, auditoria, alertas) são mais prováveis que novos tipos de divergência. `isinstance` e dicionários genéricos foram descartados por perder tipagem e espalhar decisões.

## Licença

MIT.
