from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class CompanySize(str, Enum):
    """Tamanho da empresa"""
    MICRO = "micro"  # Até 10 funcionários
    PEQUENA = "pequena"  # 10-50 funcionários
    MEDIA = "media"  # 50-200 funcionários
    GRANDE = "grande"  # 200-500 funcionários
    ENORME = "enorme"  # Mais de 500 funcionários


class MaterialType(str, Enum):
    """Tipos de material"""
    LATAO = "latao"
    AGUA = "agua"
    PAPEL = "papel"
    PLASTICO = "plastico"
    ENERGIA = "energia"


class CompanyData(BaseModel):
    """Dados da empresa"""
    size: CompanySize = Field(..., description="Tamanho da empresa")
    employees: int = Field(..., gt=0, description="Número de funcionários")
    current_material_consumption: Optional[float] = Field(0, ge=0, description="Consumo atual de material")
    industry: str = Field(..., description="Setor da empresa")


class MaterialUsage(BaseModel):
    """Uso de material"""
    type: MaterialType = Field(..., description="Tipo de material")
    quantity: float = Field(..., ge=0, description="Quantidade (toneladas, litros, kWh, etc)")
    unit: str = Field(default="toneladas", description="Unidade de medida")


class SustainabilityCalculationRequest(BaseModel):
    """Request para cálculo de sustentabilidade"""
    company: CompanyData
    proposed_materials: List[MaterialUsage] = Field(..., description="Materiais propostos")
    current_materials: Optional[List[MaterialUsage]] = Field(
        None, 
        description="Materiais atuais (para comparação)"
    )


class Benchmark(BaseModel):
    """Benchmark de referência para o tamanho da empresa"""
    company_size: CompanySize
    material_type: MaterialType
    recommended_max: float = Field(..., description="Consumo máximo recomendado")
    average_usage: float = Field(..., description="Uso médio do setor")
    excellent_threshold: float = Field(..., description="Threshold para excelente performance")


class MaterialAnalysis(BaseModel):
    """Análise de um material específico"""
    material_type: MaterialType
    proposed_quantity: float
    company_size: CompanySize
    benchmark: Benchmark
    is_eco_efficient: bool = Field(..., description="Se é ecologicamente eficiente")
    efficiency_percentage: float = Field(..., ge=0, le=100, description="Porcentagem de eficiência")
    carbon_footprint_reduction: Optional[float] = Field(None, description="Redução de pegada de carbono")
    recommendation: str = Field(..., description="Recomendação baseada na análise")


class SustainabilityAnalysisResponse(BaseModel):
    """Resposta da análise de sustentabilidade"""
    company: CompanyData
    materials_analysis: List[MaterialAnalysis]
    overall_score: float = Field(..., ge=0, le=100, description="Score geral de sustentabilidade")
    overall_recommendation: str = Field(..., description="Recomendação geral")
    is_eco_efficient: bool
    potential_savings: Optional[float] = Field(None, description="Economia potencial")
    improvements: List[str] = Field(default_factory=list, description="Sugestões de melhoria")


