# Documentação de Container - API de Clientes

Este documento descreve a arquitetura da API de Clientes.

## Diagrama de Container (C4 Nível 2)

Este diagrama mostra as unidades implantáveis (coisas que você pode "executar") que compõem sua solução.

```mermaid
C4Context
    %% Ator Externo
    Person(parceiro, "Parceiro da Empresa", "Desenvolvedor/Analista")
    System_Ext(sistema_parceiro, "Sistema do Parceiro", "Software do parceiro (ex: CRM, ERP)")

    %% Limite do nosso Sistema (agora no Render)
    System_Boundary(render_boundary, "Sistema de Vendas (Hospedado no Render)") {
        
        Container(api_flask, "API de Clientes", "Python (Flask-Smorest)", "Disponibiliza dados de clientes via JSON/HTTPS e documentação via HTML/Swagger.")
        ContainerDb(db, "Banco de Dados", "SQLite", "Armazena os dados de clientes em um arquivo persistente.")

    }

    %% Relacionamentos
    Rel(parceiro, sistema_parceiro, "Usa")
    
    %% Relacionamentos com a API
    Rel(sistema_parceiro, api_flask, "Consome", "JSON/HTTPS")
    Rel(api_flask, db, "Lê/Escreve", "SQLAlchemy")
    
    %% NOVO RELACIONAMENTO (Swagger)
    Rel(parceiro, api_flask, "Consulta Documentação", "HTML/Swagger-UI")