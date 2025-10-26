from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import health, items

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Uma API FastAPI bem estruturada",
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
app.include_router(items.router, prefix="/api/v1", tags=["Items"])


@app.on_event("startup")
async def startup_event():
    print("🚀 Iniciando a aplicação...")


@app.on_event("shutdown")
async def shutdown_event():
    print("👋 Encerrando a aplicação...")

