# Arquitetura

Fontes implementam `RecordSource`; o caso de uso indexa as entradas e delega a semântica de comparação a `MatchingPolicy`. O resultado contém razões estáveis e auditáveis, sem acoplar o domínio ao formato CSV.
