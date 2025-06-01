
# 💼 Financial Data API – Local Setup Guide

This guide walks you through running the full-stack project (FastAPI + PostgreSQL + Redis + HTML/CSS/JS frontend) either via **Docker** or **manual setup**.

---

## 🚀 Quick Start (Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/financial-data-api.git
cd financial-data-api
```

### 2. Start Backend Services (FastAPI + PostgreSQL + Redis)

```bash
docker-compose -f backend/docker-compose.yml up -d
```

### 3. Access the Services

* API: [http://localhost:8000](http://localhost:8000)
* PGAdmin: [http://localhost:5050](http://localhost:5050)
  *Credentials: `admin@admin.com` / `admin`*
* Frontend: Open `frontend/index.html` in your browser or use `live-server` (see below)

---

## 🛠 Manual Setup (Detailed)

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Environment Variables (.env)**

```bash
echo "DATABASE_URL=postgresql://postgres:postgres@localhost:5432/financial_data" > .env
echo "REDIS_URL=redis://localhost:6379" >> .env
echo "ALPHA_VANTAGE_API_KEY=your_api_key_here" >> .env
```

**Initialize Database**

```bash
alembic upgrade head
```

**Run the API**

```bash
uvicorn app.main:app --reload
```

> API will be available at [http://localhost:8000](http://localhost:8000)

---

### 2. Database (PostgreSQL) Setup

Install PostgreSQL (Ubuntu example):

```bash
sudo apt install postgresql postgresql-contrib
```

Start PostgreSQL:

```bash
sudo service postgresql start
```

Create the database:

```bash
sudo -u postgres psql
CREATE DATABASE financial_data;
\q
```

---

### 3. Redis Setup

Install Redis:

```bash
sudo apt install redis-server
```

Start Redis:

```bash
sudo service redis-server start
```

---

### 4. Frontend Setup

```bash
cd ../frontend

# Optional: Install live-server for dev preview
npm install -g live-server

# Run the frontend
live-server --port=3000
```

> Access the frontend at [http://localhost:3000](http://localhost:3000)

---

## 🔌 Connect Frontend to Backend

In `frontend/scripts/main.js`, update the backend API base URL:

```javascript
const API_BASE_URL = 'http://localhost:8000';
```

---

## 🧪 Running Backend Tests

```bash
cd backend
source venv/bin/activate

# Run tests
pytest -v

# Run with coverage
pytest --cov=app --cov-report=html
```

---

## 🌐 Access Points Summary

| Service    | URL                                                      |
| ---------- | -------------------------------------------------------- |
| API Docs   | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Frontend   | [http://localhost:3000](http://localhost:3000)           |
| PostgreSQL | postgresql://localhost:5432                              |
| Redis      | redis\://localhost:6379                                  |
| PGAdmin    | [http://localhost:5050](http://localhost:5050)           |

---

## 🚨 Troubleshooting

**Port Conflicts**
Check for processes using ports:

```bash
sudo lsof -i :8000
```

**Database Connection Issues**

```bash
psql -h localhost -U postgres -d financial_data
```

**Missing Data from Alpha Vantage**
Ensure you have a valid [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key)

**Frontend Not Connecting?**

* Check browser console (F12) for CORS errors.
* Verify `API_BASE_URL` in `main.js`.

---

## 🐳 Docker Cleanup

```bash
# Stop all services
docker-compose -f backend/docker-compose.yml down

# Optionally remove volumes
docker volume prune
```

---

Choose **Docker** for quick setup or **manual mode** for customization. Once running, your full stack is accessible at:

* **API**: [http://localhost:8000](http://localhost:8000)
* **Frontend**: [http://localhost:3000](http://localhost:3000)
