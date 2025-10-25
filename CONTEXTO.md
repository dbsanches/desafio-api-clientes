# Documentação de Arquitetura - API de Clientes

Este documento descreve o contexto da API de Clientes.

## Diagrama de Contexto (C4 Nível 1)

Este diagrama situa nossa "API de Clientes" no ambiente de vendas on-line da empresa. Ele mostra o limite do nosso sistema e quem interage com ele.

```mermaid
graph TD
    %% Define os estilos
    classDef system fill:#1168bd,stroke:#0a4883,stroke-width:2px,color:#fff;
    classDef person fill:#08427b,stroke:#0a4883,stroke-width:2px,color:#fff;
    classDef extSystem fill:#999,stroke:#666,stroke-width:2px,color:#fff;

    %% Define os elementos
    parceiro(Parceiro da Empresa)
    sistemaParceiro[Sistema do Parceiro]
    apiClientes(API de Clientes)

    %% Define as classes
    class parceiro person;
    class sistemaParceiro extSystem;
    class apiClientes system;

    %% Define as setas
    parceiro -- "Usa" --> sistemaParceiro
    sistemaParceiro -- "Gerencia dados de clientes via<br/>[JSON/HTTPS]" --> apiClientes
    
