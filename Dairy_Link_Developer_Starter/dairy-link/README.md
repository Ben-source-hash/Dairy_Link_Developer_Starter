# Dairy Link Developer Starter
Dairy Link MVP starter repository.

Stack: React + TypeScript + Vite, Python + FastAPI, PostgreSQL, Docker Compose.

## Run
1. Start PostgreSQL: `docker compose up -d db`
2. Backend:
   `cd backend`
   `python -m venv .venv`
   Windows: `.venv\Scripts\activate`
   `pip install -r requirements.txt`
   `uvicorn app.main:app --reload`
3. Frontend:
   `cd frontend`
   `npm install`
   `npm run dev`

API docs: http://localhost:8000/docs
