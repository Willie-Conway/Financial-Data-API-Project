# backend/app/routes/stocks.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..services.alpha_vantage import get_real_time_price
from ..services.cache import get_from_cache, set_in_cache
from ..database import get_db
from ..models.financial_data import FinancialData
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{symbol}")
async def get_stock_data(symbol: str, db: Session = Depends(get_db)):
    # Check cache first
    cached_data = get_from_cache(f"stock_{symbol}")
    if cached_data:
        return cached_data
    
    # If not in cache, fetch from Alpha Vantage
    stock_data = await get_real_time_price(symbol)
    if not stock_data:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    # Store in cache for 5 minutes
    set_in_cache(f"stock_{symbol}", stock_data, expire=300)
    
    return stock_data