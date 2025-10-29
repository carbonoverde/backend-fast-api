# Backend FastAPI - Análise de Sustentabilidade

Uma aplicação FastAPI especializada em análise de sustentabilidade e pegada verde, que recebe dados de formulários e calcula se o uso de materiais (latao, agua, papel, etc.) é ecologicamente econômico para o tamanho da empresa.

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
│   │   └── sustainability.py # Endpoints de sustentabilidade
│   ├── schemas/             # Schemas Pydantic
│   │   ├── __init__.py
│   │   └── sustainability.py # Schemas para análises
│   └── utils/               # Utilitários
│       ├── __init__.py
│       └── sustainability.py # Cálculos e lógica de negócio
├── tests/                   # Testes
│   ├── __init__.py
│   ├── test_health.py
│   └── test_sustainability.py
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

### Análise de Sustentabilidade
- `POST /api/v1/sustainability/analyze` - Analisa sustentabilidade de materiais
- `GET /api/v1/sustainability/benchmarks/{company_size}` - Obter benchmarks por tamanho
- `GET /api/v1/sustainability/materials` - Listar materiais disponíveis
- `GET /api/v1/sustainability/company-sizes` - Listar tamanhos de empresa
- `GET /api/v1/sustainability/example` - Exemplo de uso da API

### Exemplo de Request

```json
{
  "company": {
    "size": "media",
    "employees": 100,
    "industry": "Manufatura",
    "current_material_consumption": null
  },
  "proposed_materials": [
    {
      "type": "latao",
      "quantity": 8.5,
      "unit": "toneladas"
    },
    {
      "type": "agua",
      "quantity": 850,
      "unit": "toneladas"
    }
  ]
}
```

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

## 📖 Documentação Adicional

Para mais exemplos de uso e casos de teste, consulte:
- [EXAMPLES.md](EXAMPLES.md) - Exemplos detalhados de uso da API
- [Swagger UI](http://localhost:8000/docs) - Documentação interativa

## 📝 Próximos Passos

Melhorias sugeridas:

- [ ] Integração com banco de dados para histórico de análises
- [ ] Dashboard de métricas de sustentabilidade
- [ ] Comparação com outras empresas do setor
- [ ] Exportação de relatórios em PDF
- [ ] Autenticação e autorização
- [ ] Logging estruturado
- [ ] Rate limiting
- [ ] Cache (Redis)
- [ ] CI/CD pipeline

## 📄 Licença

Este projeto está sob a licença MIT.
