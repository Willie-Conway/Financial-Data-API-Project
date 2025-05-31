# backend/app/routes/historical.py

from fastapi import APIRouter, Depends, HTTPException
from datetime import date
from typing import List, Optional
from ..services.alpha_vantage import get_historical_data
from ..services.cache import get_from_cache, set_in_cache
from ..database import get_db
from ..models.financial_data import FinancialData
from sqlalchemy.orm import Session
import json

router = APIRouter()

@router.get("/{symbol}")
async def get_historical_stock_data(
    symbol: str, 
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    cache_key = f"historical_{symbol}_{start_date}_{end_date}"
    
    # Check cache first
    cached_data = get_from_cache(cache_key)
    if cached_data:
        return json.loads(cached_data)
    
    # If not in cache, fetch from Alpha Vantage
    historical_data = await get_historical_data(symbol, start_date, end_date)
    if not historical_data:
        raise HTTPException(status_code=404, detail="Historical data not found")
    
    # Store in cache for 1 day
    set_in_cache(cache_key, json.dumps(historical_data), expire=86400)
    
    return historical_data