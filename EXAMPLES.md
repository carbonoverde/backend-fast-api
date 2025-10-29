# Exemplos de Uso - API de Análise de Sustentabilidade

## 📊 Como Funciona

A API analisa se o uso proposto de materiais é ecologicamente eficiente baseado em:
- Tamanho da empresa (micro, pequena, media, grande, enorme)
- Tipo de material (latão, água, papel, plástico, energia)
- Benchmarks de consumo recomendado
- Comparação com médias do setor

## 🎯 Exemplos de Cenários

### Exemplo 1: Empresa Média querendo usar Latão

**Contexto:** Empresa com 100 funcionários (tamanho médio) quer usar 8 toneladas de latão por mês.

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/sustainability/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "company": {
      "size": "media",
      "employees": 100,
      "industry": "Manufatura"
    },
    "proposed_materials": [
      {
        "type": "latao",
        "quantity": 8.0,
        "unit": "toneladas"
      }
    ]
  }'
```

**Response Esperada:**
```json
{
  "company": { ... },
  "materials_analysis": [
    {
      "material_type": "latao",
      "proposed_quantity": 8.0,
      "company_size": "media",
      "benchmark": {
        "recommended_max": 10.0,
        "average_usage": 25.0,
        "excellent_threshold": 7.5
      },
      "is_eco_efficient": true,
      "efficiency_percentage": 85.0,
      "recommendation": "Bom uso de latao. Considere otimizações para alcançar excelência.",
      "carbon_footprint_reduction": null
    }
  ],
  "overall_score": 85.0,
  "is_eco_efficient": true,
  "overall_recommendation": "Bom desempenho. Continue otimizando para alcançar excelência.",
  "potential_savings": null,
  "improvements": [
    "Manter os padrões atuais e continuar monitorando"
  ]
}
```

### Exemplo 2: Empresa Pequena com Alto Consumo de Água

**Contexto:** Empresa com 30 funcionários querendo usar 300 toneladas de água por mês.

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/sustainability/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "company": {
      "size": "pequena",
      "employees": 30,
      "industry": "Têxtil"
    },
    "proposed_materials": [
      {
        "type": "agua",
        "quantity": 300,
        "unit": "toneladas"
      }
    ]
  }'
```

**Response Esperada:**
```json
{
  "materials_analysis": [
    {
      "material_type": "agua",
      "proposed_quantity": 300.0,
      "is_eco_efficient": false,
      "efficiency_percentage": 35.0,
      "recommendation": "Alto consumo de agua. Recomenda-se reduzir em pelo menos 100.00 pequena.",
      "benchmark": {
        "recommended_max": 200,
        "average_usage": 400
      }
    }
  ],
  "overall_score": 35.0,
  "is_eco_efficient": false,
  "improvements": [
    "Reduzir agua em 100.00 unidades para atingir o padrão recomendado"
  ]
}
```

### Exemplo 3: Análise Múltipla - Latão + Água + Energia

**Contexto:** Empresa grande analisando três materiais simultaneamente.

**Request:**
```json
{
  "company": {
    "size": "grande",
    "employees": 350,
    "industry": "Siderurgia"
  },
  "proposed_materials": [
    {
      "type": "latao",
      "quantity": 45,
      "unit": "toneladas"
    },
    {
      "type": "agua",
      "quantity": 4800,
      "unit": "toneladas"
    },
    {
      "type": "energia",
      "quantity": 1200,
      "unit": "MWh"
    }
  ]
}
```

### Exemplo 4: Consultar Benchmarks

Para saber os limites recomendados para seu tamanho de empresa:

```bash
curl "http://localhost:8000/api/v1/sustainability/benchmarks/media"
```

**Response:**
```json
{
  "latao": {
    "company_size": "media",
    "material_type": "latao",
    "recommended_max": 10.0,
    "average_usage": 25.0,
    "excellent_threshold": 7.5
  },
  "agua": { ... },
  "papel": { ... },
  "plastico": { ... },
  "energia": { ... }
}
```

## 🎓 Interpretação dos Resultados

### Efficiency Percentage (Porcentagem de Eficiência)
- **80-100%**: Excelente! Está no nível de excelência
- **60-80%**: Bom desempenho, dentro do recomendado
- **40-60%**: Moderado, levemente acima do recomendado
- **0-40%**: Alto consumo, precisa de redução urgente

### Is Eco Efficient (Boolean)
- **true**: O consumo está dentro do recomendado para o tamanho da empresa
- **false**: O consumo excede o recomendado

### Recommendations (Recomendações)
Cada material recebe uma recomendação específica baseada em sua performance em relação aos benchmarks.

## 🏭 Tamanhos de Empresa

| Tamanho | Funcionários | Descrição |
|---------|-------------|-----------|
| `micro` | Até 10 | Microempresa |
| `pequena` | 10-50 | Pequena empresa |
| `media` | 50-200 | Média empresa |
| `grande` | 200-500 | Grande empresa |
| `enorme` | 500+ | Mega empresa |

## 📦 Materiais Disponíveis

1. **`latao`** - Ligas metálicas de cobre e zinco (toneladas)
2. **`agua`** - Consumo de água (toneladas)
3. **`papel`** - Produtos de papel e celulose (toneladas)
4. **`plastico`** - Polímeros plásticos (toneladas)
5. **`energia`** - Consumo energético (MWh)

## 🔄 Integração com Formulário

### JavaScript/Frontend

```javascript
async function analyzeSustainability(formData) {
  const response = await fetch('http://localhost:8000/api/v1/sustainability/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      company: {
        size: formData.companySize, // "micro", "pequena", etc
        employees: parseInt(formData.employees),
        industry: formData.industry
      },
      proposed_materials: [
        {
          type: "latao",
          quantity: parseFloat(formData.lataoQuantity),
          unit: "toneladas"
        },
        {
          type: "agua",
          quantity: parseFloat(formData.aguaQuantity),
          unit: "toneladas"
        }
      ]
    })
  });
  
  return await response.json();
}

// Exemplo de uso
const result = await analyzeSustainability({
  companySize: "media",
  employees: "100",
  industry: "Manufatura",
  lataoQuantity: "8.5",
  aguaQuantity: "850"
});

if (result.is_eco_efficient) {
  alert(`✅ Ecologicamente eficiente! Score: ${result.overall_score.toFixed(1)}%`);
} else {
  alert(`⚠️ Precisa melhorar. Score: ${result.overall_score.toFixed(1)}%`);
  console.log(result.improvements);
}
```

## 🧪 Testando Localmente

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
uvicorn app.main:app --reload

# 3. Testar com curl
curl -X POST "http://localhost:8000/api/v1/sustainability/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "company": {
      "size": "pequena",
      "employees": 25,
      "industry": "Test"
    },
    "proposed_materials": [
      {
        "type": "latao",
        "quantity": 1.0,
        "unit": "toneladas"
      }
    ]
  }'
```


