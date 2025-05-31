# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import stocks, historical

app = FastAPI(
    title="Financial Data API",
    description="RESTful API for financial data with real-time stock market integration and historical analysis",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stocks.router, prefix="/api/stocks", tags=["stocks"])
app.include_router(historical.router, prefix="/api/historical", tags=["historical"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Financial Data API"}