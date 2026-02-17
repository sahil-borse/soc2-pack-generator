# SOC2 Policy Pack API (MVP)

FastAPI + MongoDB + JWT + OpenAI + DOCX/ZIP export.

## Setup

```bash
cd soc2_backend_mvp
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows PowerShell: Copy-Item .env.example .env
```

Update `.env` with:
- MONGO_URI
- JWT_SECRET
- OPENAI_API_KEY

## Run

```bash
uvicorn app.main:app --reload --port 8000
```

Swagger:
- http://localhost:8000/docs

Health:
- http://localhost:8000/api/health
```

Files:
- app/routes/* (API endpoints)
- app/services/* (business logic)
- app/ai/* (prompting + generation)
- app/utils/* (JWT/password helpers)
