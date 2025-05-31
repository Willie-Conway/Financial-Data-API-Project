from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Financial Data API"}

def test_get_stock_data():
    response = client.get("/api/stocks/AAPL")
    assert response.status_code in [200, 404]  # 404 if Alpha Vantage key is demo

def test_get_historical_data():
    response = client.get("/api/historical/AAPL")
    assert response.status_code in [200, 404]