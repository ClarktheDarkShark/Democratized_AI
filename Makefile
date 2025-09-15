.PHONY: dev test fmt db/migrate seed

dev:
	docker-compose up --build

test:
	cd backend && PYTHONPATH=. pytest
	cd frontend && npm install && npm test

fmt:
	cd backend && black .
	cd frontend && npx prettier --write .

db/migrate:
	cd backend && alembic upgrade head

seed:
	echo "seeding not implemented"
