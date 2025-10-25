# Documentação de Classe - API de Clientes

Este documento mostra a classe, seus atributos e suas principais operações.

## Diagrama de Classe (UML)

Este é o "plano de construção" do nosso Model. Ele mostra exatamente quais atributos (campos) e métodos (funções) nossa classe Cliente terá. Isso é fundamental para quem vai escrever o código e para quem vai criar o banco de dados.

```mermaid
classDiagram
    %% Classe de Dados (Modelo SQLAlchemy)
    class Cliente {
        <<Model>>
        -id: Integer
        -nome: String
        -email: String (unique)
        -telefone: String
    }

    %% Classe de Lógica (Serviço)
    class ClienteService {
        <<Service>>
        +create(novo_cliente: Cliente): Cliente
        +get_all(): list[Cliente]
        +get_by_id(id): Cliente
        +update(id, data_update: dict): Cliente
        +delete(id): bool
        +get_by_name(nome): list[Cliente]
        +count(): int
    }

    %% Relacionamento
    ClienteService ..> Cliente : "Usa (lê/escreve)"