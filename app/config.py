from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Informações do projeto
    PROJECT_NAME: str = "Backend FastAPI"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Configurações do servidor
    API_V1_STR: str = "/api/v1"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # Database (se necessário no futuro)
    DATABASE_URL: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

