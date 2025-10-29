# 🚀 Guia Rápido de Início

## Instalação e Execução

```bash
# 1. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Iniciar servidor
uvicorn app.main:app --reload
```

## 📡 Teste Rápido

Acesse: http://localhost:8000/docs

## 🎯 Primeiro Request

### Via cURL
```bash
curl -X POST "http://localhost:8000/api/v1/sustainability/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "company": {
      "size": "pequena",
      "employees": 25,
      "industry": "Manufatura"
    },
    "proposed_materials": [
      {
        "type": "latao",
        "quantity": 1.5,
        "unit": "toneladas"
      }
    ]
  }'
```

### Via Python
```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/sustainability/analyze",
    json={
        "company": {
            "size": "pequena",
            "employees": 25,
            "industry": "Manufatura"
        },
        "proposed_materials": [
            {
                "type": "latao",
                "quantity": 1.5,
                "unit": "toneladas"
            }
        ]
    }
)

print(response.json()["overall_score"])  # Score de 0-100
print(response.json()["is_eco_efficient"])  # True ou False
```

## ✅ Checklist de Integração

- [ ] Receber dados do formulário (tamanho empresa, materiais)
- [ ] Enviar POST para `/api/v1/sustainability/analyze`
- [ ] Mostrar resultado (`overall_score`, `is_eco_efficient`)
- [ ] Exibir recomendações (`recommendations`, `improvements`)
- [ ] Destacar materiais que precisam melhoria

## 📊 Interpretação Rápida

| Score | Status | Ação |
|-------|--------|------|
| 80-100 | ✅ Excelente | Manter padrões |
| 60-80 | ✓ Bom | Otimizar |
| 40-60 | ⚠️ Moderado | Melhorar |
| 0-40 | ❌ Alto | Reduzir urgente |

## 🔗 Links Úteis

- Documentação: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- Benchmarks: http://localhost:8000/api/v1/sustainability/benchmarks/media


