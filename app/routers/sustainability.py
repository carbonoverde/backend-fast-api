from fastapi import APIRouter, HTTPException
from app.schemas.sustainability import (
    SustainabilityCalculationRequest,
    SustainabilityAnalysisResponse,
    MaterialType,
    CompanySize,
)
from app.utils.sustainability import analyze_sustainability
from typing import List

router = APIRouter(prefix="/sustainability", tags=["Sustentabilidade"])


@router.post(
    "/analyze",
    response_model=SustainabilityAnalysisResponse,
    summary="Analisar sustentabilidade de materiais",
    description="Analisa se o uso proposto de materiais é ecologicamente eficiente para o tamanho da empresa"
)
def analyze_materials(request: SustainabilityCalculationRequest):
    """
    Endpoint principal para análise de sustentabilidade.
    
    Recebe dados da empresa e materiais propostos e retorna:
    - Se o uso é ecologicamente econômico
    - Score de eficiência (0-100)
    - Recomendações específicas por material
    - Melhorias sugeridas
    """
    try:
        analysis = analyze_sustainability(
            company=request.company,
            proposed_materials=request.proposed_materials
        )
        
        return analysis
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao analisar: {str(e)}")


@router.get(
    "/benchmarks/{company_size}",
    summary="Obter benchmarks de referência",
    description="Retorna os benchmarks de referência para um tamanho específico de empresa"
)
def get_benchmarks(company_size: CompanySize):
    """
    Retorna os benchmarks de referência para consumo de materiais
    baseado no tamanho da empresa.
    
    Os benchmarks incluem:
    - Consumo máximo recomendado
    - Uso médio do setor
    - Threshold para excelência
    """
    from app.utils.sustainability import BENCHMARKS
    
    if company_size not in BENCHMARKS:
        raise HTTPException(
            status_code=404,
            detail=f"Benchmarks não encontrados para tamanho: {company_size}"
        )
    
    return BENCHMARKS[company_size]


@router.get(
    "/materials",
    summary="Listar tipos de materiais disponíveis"
)
def list_materials():
    """
    Lista todos os tipos de materiais que podem ser analisados
    """
    return {
        "materials": [
            {
                "type": mt.value,
                "description": get_material_description(mt)
            }
            for mt in MaterialType
        ]
    }


def get_material_description(material_type: MaterialType) -> str:
    """Retorna descrição amigável do tipo de material"""
    descriptions = {
        MaterialType.LATAO: "Ligas metálicas de cobre e zinco",
        MaterialType.AGUA: "Consumo de água",
        MaterialType.PAPEL: "Produtos de papel e celulose",
        MaterialType.PLASTICO: "Polímeros plásticos",
        MaterialType.ENERGIA: "Consumo de energia (elétrica, gás, etc.)"
    }
    return descriptions.get(material_type, "Material genérico")


@router.get(
    "/company-sizes",
    summary="Listar tamanhos de empresa disponíveis"
)
def list_company_sizes():
    """
    Lista todos os tamanhos de empresa disponíveis com suas descrições
    """
    return {
        "company_sizes": [
            {
                "size": cs.value,
                "description": get_company_size_description(cs)
            }
            for cs in CompanySize
        ]
    }


def get_company_size_description(size: CompanySize) -> str:
    """Retorna descrição amigável do tamanho da empresa"""
    descriptions = {
        CompanySize.MICRO: "Até 10 funcionários",
        CompanySize.PEQUENA: "10-50 funcionários",
        CompanySize.MEDIA: "50-200 funcionários",
        CompanySize.GRANDE: "200-500 funcionários",
        CompanySize.ENORME: "Mais de 500 funcionários"
    }
    return descriptions.get(size, "Tamanho não especificado")


@router.get(
    "/example",
    summary="Exemplo de uso da API",
    description="Retorna um exemplo de request para análise de sustentabilidade"
)
def get_example():
    """
    Retorna um exemplo de como usar o endpoint de análise
    """
    return {
        "example_request": {
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
        },
        "note": "Envie este JSON para POST /sustainability/analyze"
    }


