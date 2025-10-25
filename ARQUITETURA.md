# Documentação de Arquitetura - API de Clientes

Este documento descreve a arquitetura da API de Clientes.

## Diagrama de Componentes (C4 Nível 3)

Este diagrama detalha a arquitetura interna da aplicação, seguindo o padrão MVC.

```mermaid
graph TD
    %% Define os estilos
    classDef component fill:#85b8fb,stroke:#0a4883,stroke-width:2px,color:#333;
    classDef extSystem fill:#999,stroke:#666,stroke-width:2px,color:#fff;
    classDef database fill:#dbb5b5,stroke:#a04a4a,stroke-width:2px,color:#333;

    %% Elementos
    sistemaParceiro[Sistema do Parceiro]

    subgraph api_subgraph [API de Clientes]
        direction TB
        
        controller(Cliente Controller - Componente - flask-smorest Recebe requisições HTTP. Usa Schema para deserializar.)
        
        %% NOVO COMPONENTE
        service(Cliente Service - Componente Contém a lógica de negócio. Ex: Validação de email duplicado)
        
        schema(Cliente Schema - Componente - Marshmallow Define a View dos dados. Valida o formato JSON a Objeto)
        
        model(Cliente Model - Componente - SQLAlchemy Representa a tabela do banco de dados.)
        
        db[(database.db - Container - SQLite)]

        %% Relacionamentos
        controller -- "Usa para deserializar" --> schema
        controller -- "Chama" --> service
        service -- "Usa" --> model
        model -- "Lê/Escreve" --> db
    end

    %% Relacionamento Externo
    sistemaParceiro -- "Envia Requisição JSON/HTTPS" --> controller

    %% Aplica classes
    class sistemaParceiro extSystem;
    class controller component;
    class service component;
    class schema component;
    class model component;
    class db database;