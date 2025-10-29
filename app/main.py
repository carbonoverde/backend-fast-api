from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import health, sustainability

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API FastAPI para Análise de Sustentabilidade e Pegada Verde",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(health.router, tags=["Health"])
app.include_router(sustainability.router, prefix="/api/v1", tags=["Sustentabilidade"])


@app.on_event("startup")
async def startup_event():
    print("🚀 Iniciando a aplicação...")


@app.on_event("shutdown")
async def shutdown_event():
    print("👋 Encerrando a aplicação...")

