"""
Utilitários para cálculos de sustentabilidade e pegada verde
"""
from typing import List
from app.schemas.sustainability import (
    MaterialType,
    CompanySize,
    MaterialUsage,
    Benchmark,
    MaterialAnalysis,
    SustainabilityAnalysisResponse,
    CompanyData,
)


# Benchmarks de referência por tipo de material e tamanho da empresa
BENCHMARKS = {
    CompanySize.MICRO: {
        MaterialType.LATAO: Benchmark(
            company_size=CompanySize.MICRO,
            material_type=MaterialType.LATAO,
            recommended_max=0.5,  # 0.5 toneladas
            average_usage=1.0,
            excellent_threshold=0.3
        ),
        MaterialType.AGUA: Benchmark(
            company_size=CompanySize.MICRO,
            material_type=MaterialType.AGUA,
            recommended_max=50,  # 50 toneladas
            average_usage=100,
            excellent_threshold=30
        ),
        MaterialType.PAPEL: Benchmark(
            company_size=CompanySize.MICRO,
            material_type=MaterialType.PAPEL,
            recommended_max=2.0,
            average_usage=4.0,
            excellent_threshold=1.5
        ),
        MaterialType.PLASTICO: Benchmark(
            company_size=CompanySize.MICRO,
            material_type=MaterialType.PLASTICO,
            recommended_max=1.0,
            average_usage=2.5,
            excellent_threshold=0.5
        ),
        MaterialType.ENERGIA: Benchmark(
            company_size=CompanySize.MICRO,
            material_type=MaterialType.ENERGIA,
            recommended_max=10,  # 10 MWh
            average_usage=20,
            excellent_threshold=7
        ),
    },
    CompanySize.PEQUENA: {
        MaterialType.LATAO: Benchmark(
            company_size=CompanySize.PEQUENA,
            material_type=MaterialType.LATAO,
            recommended_max=2.0,
            average_usage=5.0,
            excellent_threshold=1.5
        ),
        MaterialType.AGUA: Benchmark(
            company_size=CompanySize.PEQUENA,
            material_type=MaterialType.AGUA,
            recommended_max=200,
            average_usage=400,
            excellent_threshold=150
        ),
        MaterialType.PAPEL: Benchmark(
            company_size=CompanySize.PEQUENA,
            material_type=MaterialType.PAPEL,
            recommended_max=10.0,
            average_usage=20.0,
            excellent_threshold=7.0
        ),
        MaterialType.PLASTICO: Benchmark(
            company_size=CompanySize.PEQUENA,
            material_type=MaterialType.PLASTICO,
            recommended_max=5.0,
            average_usage=12.0,
            excellent_threshold=3.0
        ),
        MaterialType.ENERGIA: Benchmark(
            company_size=CompanySize.PEQUENA,
            material_type=MaterialType.ENERGIA,
            recommended_max=50,
            average_usage=100,
            excellent_threshold=35
        ),
    },
    CompanySize.MEDIA: {
        MaterialType.LATAO: Benchmark(
            company_size=CompanySize.MEDIA,
            material_type=MaterialType.LATAO,
            recommended_max=10.0,
            average_usage=25.0,
            excellent_threshold=7.5
        ),
        MaterialType.AGUA: Benchmark(
            company_size=CompanySize.MEDIA,
            material_type=MaterialType.AGUA,
            recommended_max=1000,
            average_usage=2000,
            excellent_threshold=750
        ),
        MaterialType.PAPEL: Benchmark(
            company_size=CompanySize.MEDIA,
            material_type=MaterialType.PAPEL,
            recommended_max=50.0,
            average_usage=100.0,
            excellent_threshold=35.0
        ),
        MaterialType.PLASTICO: Benchmark(
            company_size=CompanySize.MEDIA,
            material_type=MaterialType.PLASTICO,
            recommended_max=25.0,
            average_usage=60.0,
            excellent_threshold=15.0
        ),
        MaterialType.ENERGIA: Benchmark(
            company_size=CompanySize.MEDIA,
            material_type=MaterialType.ENERGIA,
            recommended_max=250,
            average_usage=500,
            excellent_threshold=175
        ),
    },
    CompanySize.GRANDE: {
        MaterialType.LATAO: Benchmark(
            company_size=CompanySize.GRANDE,
            material_type=MaterialType.LATAO,
            recommended_max=50.0,
            average_usage=125.0,
            excellent_threshold=37.5
        ),
        MaterialType.AGUA: Benchmark(
            company_size=CompanySize.GRANDE,
            material_type=MaterialType.AGUA,
            recommended_max=5000,
            average_usage=10000,
            excellent_threshold=3750
        ),
        MaterialType.PAPEL: Benchmark(
            company_size=CompanySize.GRANDE,
            material_type=MaterialType.PAPEL,
            recommended_max=250.0,
            average_usage=500.0,
            excellent_threshold=175.0
        ),
        MaterialType.PLASTICO: Benchmark(
            company_size=CompanySize.GRANDE,
            material_type=MaterialType.PLASTICO,
            recommended_max=125.0,
            average_usage=300.0,
            excellent_threshold=75.0
        ),
        MaterialType.ENERGIA: Benchmark(
            company_size=CompanySize.GRANDE,
            material_type=MaterialType.ENERGIA,
            recommended_max=1250,
            average_usage=2500,
            excellent_threshold=875
        ),
    },
    CompanySize.ENORME: {
        MaterialType.LATAO: Benchmark(
            company_size=CompanySize.ENORME,
            material_type=MaterialType.LATAO,
            recommended_max=250.0,
            average_usage=625.0,
            excellent_threshold=187.5
        ),
        MaterialType.AGUA: Benchmark(
            company_size=CompanySize.ENORME,
            material_type=MaterialType.AGUA,
            recommended_max=25000,
            average_usage=50000,
            excellent_threshold=18750
        ),
        MaterialType.PAPEL: Benchmark(
            company_size=CompanySize.ENORME,
            material_type=MaterialType.PAPEL,
            recommended_max=1250.0,
            average_usage=2500.0,
            excellent_threshold=875.0
        ),
        MaterialType.PLASTICO: Benchmark(
            company_size=CompanySize.ENORME,
            material_type=MaterialType.PLASTICO,
            recommended_max=625.0,
            average_usage=1500.0,
            excellent_threshold=375.0
        ),
        MaterialType.ENERGIA: Benchmark(
            company_size=CompanySize.ENORME,
            material_type=MaterialType.ENERGIA,
            recommended_max=6250,
            average_usage=12500,
            excellent_threshold=4375
        ),
    },
}


def get_benchmark(company_size: CompanySize, material_type: MaterialType) -> Benchmark:
    """Retorna o benchmark para um tipo de material e tamanho de empresa"""
    return BENCHMARKS[company_size][material_type]


def calculate_efficiency_percentage(quantity: float, benchmark: Benchmark) -> float:
    """
    Calcula a porcentagem de eficiência baseada nos benchmarks
    
    Args:
        quantity: Quantidade proposta do material
        benchmark: Benchmark de referência
        
    Returns:
        Porcentagem de eficiência (0-100)
    """
    if quantity <= benchmark.excellent_threshold:
        # Excelente performance: 80-100%
        ratio = quantity / benchmark.excellent_threshold if benchmark.excellent_threshold > 0 else 0
        return max(80, 100 - (ratio * 20))
    
    elif quantity <= benchmark.recommended_max:
        # Boa performance: 60-80%
        range_size = benchmark.recommended_max - benchmark.excellent_threshold
        if range_size <= 0:
            return 70
        ratio = (quantity - benchmark.excellent_threshold) / range_size
        return 80 - (ratio * 20)
    
    elif quantity <= benchmark.average_usage:
        # Performance média: 40-60%
        range_size = benchmark.average_usage - benchmark.recommended_max
        if range_size <= 0:
            return 50
        ratio = (quantity - benchmark.recommended_max) / range_size
        return 60 - (ratio * 20)
    
    else:
        # Performance abaixo da média: 0-40%
        excess = quantity - benchmark.average_usage
        # Para cada unidade acima da média, reduz 5% até um mínimo de 0%
        reduction = min(40, excess / 10 * 5)
        return max(0, 40 - reduction)


def is_eco_efficient(quantity: float, benchmark: Benchmark) -> bool:
    """Determina se o uso é ecologicamente eficiente"""
    return quantity <= benchmark.recommended_max


def generate_recommendation(analysis: MaterialAnalysis) -> str:
    """Gera uma recomendação baseada na análise do material"""
    if analysis.efficiency_percentage >= 80:
        return f"Excelente! Uso de {analysis.material_type.value} está dentro dos padrões de excelência."
    elif analysis.efficiency_percentage >= 60:
        return f"Bom uso de {analysis.material_type.value}. Considere otimizações para alcançar excelência."
    elif analysis.efficiency_percentage >= 40:
        return f"Uso moderado de {analysis.material_type.value}. Há espaço para melhorias significativas."
    else:
        reduction = analysis.proposed_quantity - analysis.benchmark.recommended_max
        return f"Alto consumo de {analysis.material_type.value}. Recomenda-se reduzir em pelo menos {reduction:.2f} {analysis.benchmark.company_size.value}."


def analyze_material(
    material: MaterialUsage,
    company_size: CompanySize
) -> MaterialAnalysis:
    """
    Analisa um material específico
    
    Args:
        material: Informações do material
        company_size: Tamanho da empresa
        
    Returns:
        Análise do material
    """
    benchmark = get_benchmark(company_size, material.type)
    efficiency = calculate_efficiency_percentage(material.quantity, benchmark)
    is_eco = is_eco_efficient(material.quantity, benchmark)
    
    # Calcular redução de carbono aproximada (se eficiente)
    carbon_reduction = None
    if is_eco:
        excess_over_excellent = material.quantity - benchmark.excellent_threshold
        if excess_over_excellent < 0:
            # Está abaixo do threshold excelente
            material_types = {
                MaterialType.LATAO: 2.5,  # kg CO2 por kg de latão
                MaterialType.AGUA: 0.001,
                MaterialType.PAPEL: 1.8,
                MaterialType.PLASTICO: 2.5,
                MaterialType.ENERGIA: 0.5
            }
            carbon_per_unit = material_types.get(material.type, 1.0)
            carbon_reduction = abs(excess_over_excellent) * carbon_per_unit * 1000  # Converter para kg
    
    analysis = MaterialAnalysis(
        material_type=material.type,
        proposed_quantity=material.quantity,
        company_size=company_size,
        benchmark=benchmark,
        is_eco_efficient=is_eco,
        efficiency_percentage=efficiency,
        carbon_footprint_reduction=carbon_reduction,
        recommendation=""
    )
    
    # Gerar recomendação
    analysis.recommendation = generate_recommendation(analysis)
    
    return analysis


def calculate_sustainability_score(analyses: List[MaterialAnalysis]) -> float:
    """Calcula o score geral de sustentabilidade"""
    if not analyses:
        return 0
    
    total_score = sum(analysis.efficiency_percentage for analysis in analyses)
    return total_score / len(analyses)


def generate_overall_recommendation(score: float) -> str:
    """Gera uma recomendação geral baseada no score"""
    if score >= 80:
        return "Excelente! Sua empresa demonstra alto comprometimento com sustentabilidade."
    elif score >= 60:
        return "Bom desempenho. Continue otimizando para alcançar excelência."
    elif score >= 40:
        return "Performance moderada. Há oportunidades significativas de melhoria."
    else:
        return "Atenção necessária. Implemente práticas mais sustentáveis urgentemente."


def generate_improvements(analyses: List[MaterialAnalysis]) -> List[str]:
    """Gera lista de melhorias sugeridas"""
    improvements = []
    
    for analysis in analyses:
        if not analysis.is_eco_efficient:
            excess = analysis.proposed_quantity - analysis.benchmark.recommended_max
            improvements.append(
                f"Reduzir {analysis.material_type.value} em {excess:.2f} unidades para atingir o padrão recomendado"
            )
    
    if not improvements:
        improvements.append("Manter os padrões atuais e continuar monitorando")
    
    return improvements


def calculate_potential_savings(analyses: List[MaterialAnalysis]) -> float:
    """Calcula economia potencial em toneladas equivalentes"""
    if not analyses:
        return 0
    
    total_savings = 0
    for analysis in analyses:
        if not analysis.is_eco_efficient:
            excess = analysis.proposed_quantity - analysis.benchmark.recommended_max
            if excess > 0:
                total_savings += excess
    
    return total_savings


def analyze_sustainability(
    company: CompanyData,
    proposed_materials: List[MaterialUsage]
) -> SustainabilityAnalysisResponse:
    """
    Função principal para análise de sustentabilidade
    
    Args:
        company: Dados da empresa
        proposed_materials: Lista de materiais propostos
        
    Returns:
        Análise completa de sustentabilidade
    """
    # Analisar cada material
    materials_analysis = [
        analyze_material(material, company.size)
        for material in proposed_materials
    ]
    
    # Calcular score geral
    overall_score = calculate_sustainability_score(materials_analysis)
    
    # Determinar se é geralmente eficiente
    is_eco = all(analysis.is_eco_efficient for analysis in materials_analysis)
    
    # Gerar recomendação geral
    overall_recommendation = generate_overall_recommendation(overall_score)
    
    # Calcular economias potenciais
    potential_savings = calculate_potential_savings(materials_analysis)
    
    # Gerar melhorias sugeridas
    improvements = generate_improvements(materials_analysis)
    
    return SustainabilityAnalysisResponse(
        company=company,
        materials_analysis=materials_analysis,
        overall_score=overall_score,
        overall_recommendation=overall_recommendation,
        is_eco_efficient=is_eco,
        potential_savings=potential_savings if potential_savings > 0 else None,
        improvements=improvements
    )


