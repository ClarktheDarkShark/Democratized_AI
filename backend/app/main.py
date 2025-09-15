from fastapi import FastAPI

from .api.v1 import agents, approvals, connectors, health, rag, runs, tools
from .core import audit
from .core.deps import engine
from .domain.models import Base

try:
    Base.metadata.create_all(bind=engine)
except Exception:
    pass

app = FastAPI(title="Agentic Platform")
app.middleware("http")(audit.audit_middleware)

app.include_router(health.router)
app.include_router(agents.router)
app.include_router(runs.router)
app.include_router(approvals.router)
app.include_router(rag.router)
app.include_router(tools.router)
app.include_router(connectors.router)
