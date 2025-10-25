# Documentação de Arquitetura - API de Clientes

Este documento descreve a arquitetura da API de Clientes.

## Diagrama de Componentes (C4 Nível 3)

Este diagrama detalha a arquitetura interna da aplicação, seguindo o padrão MVC.

```mermaid
flowchart TD
    %% Define os estilos
    classDef component fill:#85b8fb,stroke:#0a4883,stroke-width:2px,color:#333;
    classDef extSystem fill:#999,stroke:#666,stroke-width:2px,color:#fff;
    classDef database fill:#dbb5b5,stroke:#a04a4a,stroke-width:2px,color:#333;

    %% Elementos
    sistemaParceiro["Sistema do Parceiro"]

    subgraph API_de_Clientes_Flask_App
        direction TB
        controller["Cliente Controller [Componente] Recebe requisições HTTP e orquestra."]
        view["Cliente View [Componente] Serializa/Deserializa Objetos <=> JSON"]
        model["Cliente Model [Componente] Encapsula lógica de negócio e acesso aos dados."]
        db["Banco de Dados [SQLite/PostgreSQL]"]

        %% Relacionamentos
        controller -- "Usa para (de)serializar" --> view
        controller -- "Usa para operações" --> model
        model -- "Lê/Escreve" --> db
    end

    %% Relacionamento Externo
    sistemaParceiro -- "Envia Requisição [JSON/HTTPS]" --> controller

    %% Aplica classes
    class sistemaParceiro extSystem;
    class controller component;
    class view component;
    class model component;
    class db database;