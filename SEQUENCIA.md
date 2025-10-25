# Documentação de fluxo - API de Clientes

Este documento descreve o fluxo dinâmico e a ordem das interações entre os componentes do MVC para um caso de uso específico: a criação de um novo cliente.

## Diagrama de Sequência UML (POST /clientes)

Este diagrama lê da esquerda para a direita, de cima para baixo.

```mermaid
sequenceDiagram
    participant Parceiro as Sistema do<br/>Parceiro
    participant Controller as :ClienteController<br/>(com Smorest)
    participant Schema as :ClienteSchema
    participant Service as :ClienteService
    participant Model as :Cliente (SQLA)
    participant DB as :Database

    Parceiro ->>+ Controller: 1. POST /clientes (Body: JSON)
    
    Controller ->>+ Schema: 2. @arguments(Schema) <br/> deserializar(JSON)
    Schema -->>- Controller: 3. Retorna Objeto Cliente (novo_cliente)
    
    Controller ->>+ Service: 4. create(novo_cliente)
    Service ->>+ Model: 5. db.session.add(novo_cliente)
    Model ->>+ DB: 6. INSERT INTO...
    DB -->>- Model: 7. Retorna dados (ex: ID)
    Model -->>- Service: 8. Retorna Objeto Cliente (com ID)
    Service -->>- Controller: 9. Retorna Objeto Cliente
    
    Controller ->>+ Schema: 10. @response(Schema) <br/> serializar(Objeto Cliente)
    Schema -->>- Controller: 11. Retorna JSON
    Controller -->>- Parceiro: 12. Resposta 201 (Body: JSON)