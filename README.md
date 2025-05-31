
# 📈 Financial Data API & Dashboard

![Project Banner](https://via.placeholder.com/1200x400?text=Financial+Data+API+%26+Dashboard)  


Welcome to the **Financial Data API & Dashboard** — a full-stack web application for retrieving, analyzing, and visualizing stock market data in real-time. Built with a robust FastAPI backend and a responsive JavaScript frontend, this project is perfect for investors, analysts, and developers seeking financial insights with beautiful visualizations.

---

## 🌟 Key Features

### 🔧 Backend Features
- ⚡ **Real-Time Quotes**: Retrieve up-to-date stock prices using Alpha Vantage API.
- 📅 **Historical Data**: Access daily price history for performance analysis.
- 🗃️ **Database Integration**: Store data efficiently in a PostgreSQL database.
- 🧠 **Caching**: Use Redis for caching popular symbols to boost speed.
- 🐳 **Dockerized Environment**: Run locally or in the cloud with Docker.

### 💻 Frontend Features
- 📊 **Interactive Visualizations**: Line and candlestick charts using Chart.js.
- 🔍 **Symbol Search**: Lookup stocks by ticker.
- 📆 **Date Range Filter**: Customize analysis periods for specific timeframes.
- 📱 **Responsive UI**: Works seamlessly across desktop and mobile devices.

---

## 🛠️ Tech Stack

| 🧩 Layer        | ⚙️ Technology                              |
|----------------|--------------------------------------------|
| **Backend**     | Python, FastAPI, PostgreSQL, Redis         |
| **Frontend**    | HTML5, CSS3, JavaScript, Chart.js          |
| **DevOps**      | Docker, Docker Compose, GitHub Actions     |
| **API Provider**| Alpha Vantage                              |
| **Deployment**  | GitHub Pages (Frontend), Render/Docker (API)|

---

## 🚀 Deployment Options

### 🌐 Frontend via GitHub Pages

1. Push your `frontend/` code to your GitHub repository.
2. Enable GitHub Pages under your repo's Settings > Pages.
3. Your site will be live at:  
   `https://<your-username>.github.io/financial-data-api`

---

### 🐳 Backend Deployment Options

#### Option 1: Docker Compose (Local or VPS)

```bash
cd backend
docker-compose up -d
````

This command spins up:

* FastAPI server
* PostgreSQL database
* Redis cache

Ensure `docker` and `docker-compose` are installed on your machine.

#### Option 2: Render.com

1. Create an account at [render.com](https://render.com).
2. Connect your GitHub repo.
3. Add the following **environment variables**:

```env
DATABASE_URL=your_postgres_url
REDIS_URL=your_redis_url
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
```

4. Deploy and monitor from the Render dashboard.

---

## 🧑‍💻 Local Development Setup

### Prerequisites

* Python 3.9+
* Node.js (for frontend live server)
* PostgreSQL
* Redis
* Git

---

### 🔁 Backend Setup

```bash
# Clone the repository
git clone https://github.com/your-username/financial-data-api.git
cd financial-data-api/backend

# Create a Python virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables
echo "DATABASE_URL=postgresql://postgres:postgres@localhost:5432/financial_data" > .env
echo "REDIS_URL=redis://localhost:6379" >> .env
echo "ALPHA_VANTAGE_API_KEY=your_key" >> .env

# Apply migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

---

### 🎨 Frontend Setup

```bash
cd ../frontend

# Install live-server globally (if not installed)
npm install -g live-server

# Launch development server
live-server --port=3000
```

---

## 🌐 API Endpoints Reference

| Endpoint                   | Method | Description                                         |
| -------------------------- | ------ | --------------------------------------------------- |
| `/api/stocks/{symbol}`     | GET    | Get the latest stock quote for a given symbol       |
| `/api/historical/{symbol}` | GET    | Retrieve historical data (optionally by date range) |

### 📦 Sample JSON Response

```json
{
  "symbol": "AAPL",
  "price": "175.34",
  "change": "+1.23",
  "change_percent": "+0.71%"
}
```

---

## 🗃️ Database Schema Overview

**Table: `financial_data`**

| Column        | Data Type | Description                 |
| ------------- | --------- | --------------------------- |
| `id`          | INT       | Primary Key, auto-increment |
| `symbol`      | VARCHAR   | Stock ticker symbol         |
| `date`        | DATE      | Trading day                 |
| `open_price`  | FLOAT     | Price at market open        |
| `close_price` | FLOAT     | Price at market close       |
| `volume`      | INT       | Shares traded on that day   |

Database is created automatically via Alembic migrations.

---

## 🤝 Contribution Guide

We welcome contributions from the open-source community! Follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit:

   ```bash
   git commit -m "Add feature: YourFeatureName"
   ```
4. Push to your fork:

   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a Pull Request 📬

---

## 🧪 Future Improvements

* 🧠 Add predictive analytics using machine learning
* 🌍 Support for global market indices
* 🔐 OAuth authentication for personalized dashboards
* 📅 Scheduler for automatic daily updates

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
Feel free to fork, contribute, and use in personal or commercial projects.

---

## 📬 Contact

**Your Name**
📧 [hire.willie.conway@gmail.com](mailto:hire.willie.conway@gmail.com)
🔗 GitHub Repo: [github.com/Willie-Conway/financial-data-api](https://github.com/Willie-Conway/financial-data-api)

---

## 🙏 Acknowledgments

* 💹 [Alpha Vantage](https://www.alphavantage.co/) for free stock market data
* 🐍 [FastAPI](https://fastapi.tiangolo.com/) for building high-performance APIs
* 📊 [Chart.js](https://www.chartjs.org/) for dynamic charts
* 🐳 Docker for containerization

