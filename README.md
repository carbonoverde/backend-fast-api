# Backend FastAPI

Uma aplicação FastAPI bem estruturada com arquitetura modular e pronta para escalar.

## 🏗️ Estrutura do Projeto

```
backend-fast-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicação principal
│   ├── config.py            # Configurações
│   ├── routers/             # Endpoints da API
│   │   ├── __init__.py
│   │   ├── health.py        # Endpoints de saúde
│   │   └── items.py         # Endpoints de items
│   ├── models/              # Modelos de dados
│   │   ├── __init__.py
│   │   └── item.py
│   └── schemas/             # Schemas Pydantic
│       ├── __init__.py
│       └── item.py
├── tests/                   # Testes
│   ├── __init__.py
│   ├── test_health.py
│   └── test_items.py
├── main.py                  # Ponto de entrada (legacy)
├── requirements.txt         # Dependências de produção
├── requirements-dev.txt     # Dependências de desenvolvimento
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore
└── README.md

```

## 🚀 Instalação

### 1. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements-dev.txt
```

### 3. Configurar variáveis de ambiente

```bash
cp .env.example .env
# Editar .env conforme necessário
```

## 🎯 Executando a Aplicação

### Desenvolvimento

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Produção

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📚 Documentação da API

Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🧪 Testes

Execute os testes com pytest:

```bash
pytest
```

Com coverage:

```bash
pytest --cov=app tests/
```

## 📋 Endpoints Disponíveis

### Health Check
- `GET /health` - Verifica a saúde da API
- `GET /` - Informações gerais da API

### Items (CRUD)
- `GET /api/v1/items` - Lista todos os items
- `GET /api/v1/items/{item_id}` - Busca item por ID
- `POST /api/v1/items` - Cria novo item
- `PUT /api/v1/items/{item_id}` - Atualiza item
- `DELETE /api/v1/items/{item_id}` - Deleta item

## 🔧 Configuração

As configurações podem ser ajustadas através do arquivo `.env` ou variáveis de ambiente:

- `PROJECT_NAME`: Nome do projeto
- `VERSION`: Versão da API
- `DEBUG`: Modo debug
- `HOST`: Host do servidor
- `PORT`: Porta do servidor
- `ALLOWED_ORIGINS`: Origens permitidas para CORS
- `DATABASE_URL`: URL do banco de dados (opcional)

## 📦 Stack Tecnológica

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI
- **Pytest**: Framework de testes

## 🏆 Boas Práticas Implementadas

- ✅ Estrutura modular e organizada
- ✅ Separação de responsabilidades (routers, models, schemas)
- ✅ Configuração via environment variables
- ✅ Documentação automática com Swagger
- ✅ Validação de dados com Pydantic
- ✅ Tratamento de erros HTTP
- ✅ CORS configurado
- ✅ Testes automatizados
- ✅ Type hints

## 📝 Notas

Este é um projeto base e pode ser expandido conforme necessário. Algumas melhorias futuras:

- [ ] Integração com banco de dados (SQLAlchemy, MongoDB, etc.)
- [ ] Autenticação e autorização
- [ ] Logging estruturado
- [ ] Rate limiting
- [ ] Cache (Redis)
- [ ] CI/CD pipeline

## 📄 Licença

Este projeto está sob a licença MIT.
