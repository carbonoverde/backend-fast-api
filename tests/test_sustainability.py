from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_analyze_sustainability_success():
    """Testa análise de sustentabilidade com dados válidos"""
    request_data = {
        "company": {
            "size": "media",
            "employees": 100,
            "industry": "Manufatura",
            "current_material_consumption": None
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
    
    response = client.post("/api/v1/sustainability/analyze", json=request_data)
    
    assert response.status_code == 200
    data = response.json()
    
    # Verificar estrutura da resposta
    assert "company" in data
    assert "materials_analysis" in data
    assert "overall_score" in data
    assert "is_eco_efficient" in data
    assert "improvements" in data
    
    # Verificar estrutura da análise de materiais
    assert len(data["materials_analysis"]) == 2
    for material_analysis in data["materials_analysis"]:
        assert "material_type" in material_analysis
        assert "efficiency_percentage" in material_analysis
        assert "is_eco_efficient" in material_analysis
        assert "recommendation" in material_analysis


def test_analyze_sustainability_excellent_performance():
    """Testa análise com performance excelente"""
    request_data = {
        "company": {
            "size": "pequena",
            "employees": 25,
            "industry": "Tecnologia",
            "current_material_consumption": None
        },
        "proposed_materials": [
            {
                "type": "latao",
                "quantity": 0.8,
                "unit": "toneladas"
            },
            {
                "type": "agua",
                "quantity": 80,
                "unit": "toneladas"
            }
        ]
    }
    
    response = client.post("/api/v1/sustainability/analyze", json=request_data)
    
    assert response.status_code == 200
    data = response.json()
    
    # Performance excelente deve ter score alto
    assert data["overall_score"] >= 70
    assert all(m["is_eco_efficient"] for m in data["materials_analysis"])


def test_get_benchmarks():
    """Testa obtenção de benchmarks"""
    response = client.get("/api/v1/sustainability/benchmarks/media")
    
    assert response.status_code == 200
    data = response.json()
    
    # Verificar que tem benchmarks para todos os tipos de material
    assert "latao" in data
    assert "agua" in data
    assert "papel" in data


def test_list_materials():
    """Testa listagem de materiais"""
    response = client.get("/api/v1/sustainability/materials")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "materials" in data
    assert len(data["materials"]) > 0


def test_list_company_sizes():
    """Testa listagem de tamanhos de empresa"""
    response = client.get("/api/v1/sustainability/company-sizes")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "company_sizes" in data
    assert len(data["company_sizes"]) == 5


def test_get_example():
    """Testa obtenção de exemplo"""
    response = client.get("/api/v1/sustainability/example")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "example_request" in data


def test_analyze_invalid_material():
    """Testa com material inválido"""
    request_data = {
        "company": {
            "size": "media",
            "employees": 100,
            "industry": "Manufatura"
        },
        "proposed_materials": [
            {
                "type": "invalid_material",
                "quantity": 100,
                "unit": "toneladas"
            }
        ]
    }
    
    response = client.post("/api/v1/sustainability/analyze", json=request_data)
    
    # Deve retornar erro de validação
    assert response.status_code in [422, 400]


def test_carbon_footprint_calculation():
    """Testa cálculo de redução de carbono"""
    request_data = {
        "company": {
            "size": "pequena",
            "employees": 30,
            "industry": "Sustentável"
        },
        "proposed_materials": [
            {
                "type": "latao",
                "quantity": 0.5,
                "unit": "toneladas"
            }
        ]
    }
    
    response = client.post("/api/v1/sustainability/analyze", json=request_data)
    
    assert response.status_code == 200
    data = response.json()
    
    # Verificar que há cálculo de redução de carbono
    material_analysis = data["materials_analysis"][0]
    if material_analysis.get("carbon_footprint_reduction") is not None:
        assert material_analysis["carbon_footprint_reduction"] >= 0


