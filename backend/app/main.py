from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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


@app.get("/", include_in_schema=False)
async def root() -> HTMLResponse:
    """Serve a simple landing page so the app isn't 404 at root."""
    html_content = (
        "<html><head><title>Agentic Platform API</title></head>"
        "<body><h1>Agentic Platform API</h1>"
        "<p>Visit <a href='/docs'>/docs</a> for API documentation.</p>"
        "</body></html>"
    )
    return HTMLResponse(content=html_content)

app.include_router(health.router)
app.include_router(agents.router)
app.include_router(runs.router)
app.include_router(approvals.router)
app.include_router(rag.router)
app.include_router(tools.router)
app.include_router(connectors.router)
