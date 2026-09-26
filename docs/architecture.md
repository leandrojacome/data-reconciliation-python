# Arquitetura

## Contexto e linguagem

Bounded context **Reconciliação de Registros**. `Record` representa o registro canônico; `Decimal` e moeda compõem o valor monetário. `MissingRecord` e `RecordMismatch` são divergências de domínio com invariantes estruturais distintas.

## Fronteiras

- **Domínio:** registros, divergências e contrato do Visitor.
- **Aplicação:** `ReconcileRecords` coordena fontes e política de matching.
- **Infraestrutura:** adaptadores CSV/memória e projeções de relatório.

## Padrões e alternativas

- **Strategy:** `MatchingPolicy` varia tolerância sem condicionais no caso de uso. Uma flag `tolerant=True` foi descartada por esconder regras monetárias.
- **Adapter:** CSV é detalhe substituível; parsing dentro do caso de uso foi descartado.
- **Visitor:** cada divergência aceita projeções independentes como `SummaryVisitor`. `isinstance` espalhado em relatórios foi descartado porque duplicaria dispatch e violaria aberto/fechado ao adicionar projeções.

O Visitor é apropriado porque o conjunto de divergências é pequeno/estável e as operações de saída tendem a crescer. Se os tipos variassem mais que as projeções, pattern matching seria mais simples.
