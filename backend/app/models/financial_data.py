# backend/app/models/financial_data.py

from sqlalchemy import Column, Integer, String, Float, Date
from .base import Base

class FinancialData(Base):
    __tablename__ = "financial_data"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    date = Column(Date)
    open_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Integer)
