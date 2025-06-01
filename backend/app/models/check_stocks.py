from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .financial_data import FinancialData
from .base import Base  # if you need this too




# Setup database connection and session
engine = create_engine("postgresql://postgres:postgres@localhost:5432/financial_data")

# Make sure tables exist, create if not
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Query first 10 stocks
stocks = session.query(FinancialData).limit(10).all()

for stock in stocks:
    print(f"Symbol: {stock.symbol}, Date: {stock.date}, Open: {stock.open_price}, Close: {stock.close_price}, Volume: {stock.volume}")
