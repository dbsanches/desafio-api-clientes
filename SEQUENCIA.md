# Documentação de fluxo - API de Clientes

Este documento descreve o fluxo dinâmico e a ordem das interações entre os componentes do MVC para um caso de uso específico: a criação de um novo cliente.

## Diagrama de Sequência UML (POST /clientes)

Este diagrama lê da esquerda para a direita, de cima para baixo.

```mermaid
sequenceDiagram
    participant Parceiro as Sistema do<br/>Parceiro
    participant Controller as :ClienteController
    participant View as :ClienteView
    participant Model as :ClienteModel
    participant DB as :Database

    Parceiro ->>+ Controller: 1. POST /clientes (Body: JSON)
    Controller ->>+ View: 2. deserializar(JSON)
    View -->>- Controller: 3. Retorna Objeto Cliente
    
    Controller ->>+ Model: 4. criar_cliente(Objeto Cliente)
    Model ->>+ DB: 5. INSERT INTO clientes...
    DB -->>- Model: 6. Retorna dados (ex: ID)
    Model -->>- Controller: 7. Retorna Objeto Cliente (com ID)
    
    Controller ->>+ View: 8. serializar(Objeto Cliente)
    View -->>- Controller: 9. Retorna JSON
    Controller -->>- Parceiro: 10. Resposta 201 (Body: JSON)