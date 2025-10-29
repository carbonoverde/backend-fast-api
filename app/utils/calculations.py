"""
Cálculos auxiliares para análises de sustentabilidade
"""
from typing import Dict, List
from app.schemas.sustainability import MaterialType, CompanySize


def calculate_carbon_savings(material_type: MaterialType, quantity_saved: float) -> float:
    """
    Calcula economia de carbono em kg CO2 equivalente
    
    Args:
        material_type: Tipo do material
        quantity_saved: Quantidade economizada
        
    Returns:
        Economia em kg CO2
    """
    # Fatores de emissão por unidade de material (kg CO2 por tonelada)
    emission_factors = {
        MaterialType.LATAO: 2500,  # kg CO2 por tonelada
        MaterialType.AGUA: 1.0,
        MaterialType.PAPEL: 1800,
        MaterialType.PLASTICO: 2500,
        MaterialType.ENERGIA: 500,  # kg CO2 por MWh
    }
    
    factor = emission_factors.get(material_type, 1000)
    return quantity_saved * factor


def calculate_water_intensity_by_size(size: CompanySize) -> float:
    """
    Calcula intensidade de uso de água por funcionário baseado no tamanho da empresa
    """
    intensities = {
        CompanySize.MICRO: 5.0,  # toneladas por funcionário
        CompanySize.PEQUENA: 8.0,
        CompanySize.MEDIA: 20.0,
        CompanySize.GRANDE: 25.0,
        CompanySize.ENORME: 50.0,
    }
    return intensities.get(size, 10.0)


def get_material_units(material_type: MaterialType) -> str:
    """
    Retorna a unidade padrão para cada tipo de material
    """
    units = {
        MaterialType.LATAO: "toneladas",
        MaterialType.AGUA: "toneladas",
        MaterialType.PAPEL: "toneladas",
        MaterialType.PLASTICO: "toneladas",
        MaterialType.ENERGIA: "MWh",
    }
    return units.get(material_type, "unidades")


def validate_quantity(material_type: MaterialType, quantity: float) -> bool:
    """
    Valida se a quantidade é razoável para o tipo de material
    """
    if quantity < 0:
        return False
    
    # Limites máximos por tipo de material (para prevenir erros de input)
    max_limits = {
        MaterialType.LATAO: 10000,
        MaterialType.AGUA: 1000000,
        MaterialType.PAPEL: 50000,
        MaterialType.PLASTICO: 50000,
        MaterialType.ENERGIA: 100000,
    }
    
    limit = max_limits.get(material_type, 1000000)
    return quantity <= limit


