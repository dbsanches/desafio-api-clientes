# /api-clientes-flask/run.py

from app import create_app

# Cria a instância da nossa aplicação usando a "factory"
app = create_app()

if __name__ == '__main__':
    # Roda o servidor Flask em modo de debug (ótimo para desenvolvimento)
    app.run(debug=True, host='0.0.0.0', port=5000)