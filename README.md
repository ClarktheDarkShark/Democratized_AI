# Agentic LLM Platform MVP

This repository contains a minimal but production-quality skeleton for an IL4/IL5-ready agentic LLM platform. It demonstrates agent orchestration, secure RAG, approvals, policy enforcement, audit logging and a simple UI.

## Stack
- **Frontend**: Next.js (TypeScript)
- **API**: FastAPI (Python)
- **Worker**: RQ + Redis
- **Database**: Postgres with pgvector
- **Container orchestration**: Docker Compose

## Architecture
```
+-----------+       +-------------+       +-------------+
| Frontend  | <-->  | FastAPI API | <-->  | Postgres    |
| (Next.js) |       |  + RQ queue |       | + pgvector  |
+-----------+       +-------------+       +-------------+
        ^                    |
        |                    v
        +-------------- Worker (RQ)
```

## Quick start
1. Copy `.env.example` to `.env` and adjust variables.
2. `make dev` – starts Postgres, Redis, API, worker and frontend.
3. Visit http://localhost:3000 for the UI or http://localhost:8000/docs for API docs.

## Deploy to Heroku
The backend (API + worker) can be deployed using the included `heroku.yml`:

```bash
cd backend
heroku create agentic-platform-api
heroku addons:create heroku-postgresql:mini -a agentic-platform-api
heroku addons:create heroku-redis:mini -a agentic-platform-api
heroku stack:set container -a agentic-platform-api
heroku config:set JWT_SECRET=changeme LLM_PROVIDER=openai LLM_API_KEY=changeme VECTOR_DIM=1536 -a agentic-platform-api
cd ..
git push https://git.heroku.com/agentic-platform-api.git HEAD:main
```

Release web and worker processes:

```bash
heroku container:release web worker -a agentic-platform-api
```

Deploy the frontend separately using its Dockerfile:

```bash
cd frontend
heroku create agentic-platform-frontend
heroku config:set NEXT_PUBLIC_API_URL=https://agentic-platform-api.herokuapp.com -a agentic-platform-frontend
heroku container:push web -a agentic-platform-frontend
heroku container:release web -a agentic-platform-frontend
```

## Environment Variables
| Variable | Description |
|----------|-------------|
| `APP_ENV` | Environment name |
| `API_HOST` / `API_PORT` | API bind address |
| `POSTGRES_*` | Postgres connection info |
| `REDIS_HOST` | Redis host |
| `JWT_SECRET` | JWT signing secret |
| `LLM_PROVIDER` | `openai` or `oss` |
| `LLM_API_KEY` | Provider API key placeholder |
| `VECTOR_DIM` | Embedding dimension |

## Extending
Add new connectors or tools by implementing the abstract base classes under `backend/app/services/connectors` and `backend/app/services/tools` and registering them in the respective router.

## Security Notes
- No secrets are committed; use environment variables.
- JWT auth with role-based access control.
- Policy engine denies tool execution unless explicitly allowed.
- Audit middleware logs every request.

See [`ops/threat_model.md`](ops/threat_model.md) and [`ops/runbooks/operational_checklist.md`](ops/runbooks/operational_checklist.md) for operational guidance.
