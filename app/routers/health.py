from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Endpoint de verificação de saúde da API
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "backend-fast-api"
    }


@router.get("/")
def root():
    """
    Endpoint raiz da API
    """
    return {
        "mensagem": "Bem-vindo à sua API FastAPI!",
        "versao": "1.0.0",
        "documentação": "/docs"
    }

