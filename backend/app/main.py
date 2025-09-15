from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

from .api.v1 import agents, approvals, connectors, health, rag, runs, tools
from .core import audit
from .core.deps import engine
from .core.config import settings
from .domain.models import Base

try:
    Base.metadata.create_all(bind=engine)
except Exception:
    pass

app = FastAPI(title="Agentic Platform")
app.middleware("http")(audit.audit_middleware)


@app.get("/", include_in_schema=False)
async def root():
    """Redirect to frontend if configured, else serve minimal page."""
    if settings.frontend_url:
        return RedirectResponse(settings.frontend_url)
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
