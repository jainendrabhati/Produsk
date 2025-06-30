
# 📚 Book Review Service

A FastAPI-based backend service to manage books and their reviews, with Redis caching and a Neon-hosted PostgreSQL database.

---

## 🚀 Features

- Create and fetch books
- Add and retrieve reviews for each book
- Redis caching for fast book retrieval
- PostgreSQL (Neon) for persistent storage
- Alembic migrations for database versioning
- Pytest-based test suite

---

## ⚙️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL on Neon](https://neon.tech/)
- [Redis (local)](https://redis.io/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pytest](https://docs.pytest.org/)
- [Pydantic v2](https://docs.pydantic.dev/)

---

## 📁 Project Structure

```
book_review_service/
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # DB setup
│   └── cache.py           # Redis logic
│
├── migrations/            # Alembic migration scripts
├── tests/
│   └── test_main.py       # Pytest tests
│
├── alembic.ini            # Alembic config
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
└── README.md              # This file
```

---

## 🔧 Setup Instructions

### 🧩 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-review-service.git
cd book-review_service
```

---

### 📦 2. Create Virtual Environment

```bash
python -m venv envs
source envs/Scripts/activate  # On Windows
# Or
source envs/bin/activate      # On Mac/Linux
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🗄️ 4. Configure `.env`

Create a `.env` file and add:

```env
DATABASE_URL=postgresql+psycopg2://<user>:<password>@<neon-host>/<dbname>?sslmode=require // Replace with your DATABASE_URL
REDIS_URL=redis://localhost:6379


## 🧠 Redis Setup (Local)

Make sure Redis is running locally:

Download from: https://github.com/microsoftarchive/redis/releases  
Run: `redis-server.exe`

---

## 🗃️ Database Migrations (Alembic)

### Step 1: Initialize Alembic
```bash
alembic init migrations
```

### Step 2: Autogenerate migration
```bash
alembic revision --autogenerate -m "initial"
```

### Step 3: Apply migrations
```bash
alembic upgrade head
```

---

## 🚀 Run the Server

```bash
uvicorn app.main:app --reload
```

Then visit:  
📄 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – interactive Swagger UI

---

## 🧪 Run Tests

```bash
# If you're using imports like "from app.main import app"
set PYTHONPATH=.
pytest

---

## 📌 Notes

- Redis is used to cache the `/books` response.
- PostgreSQL is hosted on [Neon.tech](https://neon.tech).
- Alembic manages DB schema changes.
- Tests use FastAPI's `TestClient` and are isolated from real DB operations.

---

## 🧑‍💻 Author

**Jainendra Bhati**  

---
