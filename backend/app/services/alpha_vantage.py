# backend/app/services/alpha_vantage.py

import os
import aiohttp
from datetime import date
from typing import Optional, Dict, Any

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "demo")

async def get_real_time_price(symbol: str) -> Dict[str, Any]:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data.get("Global Quote", {})

async def get_historical_data(
    symbol: str, 
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None
) -> Dict[str, Any]:
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={ALPHA_VANTAGE_API_KEY}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            time_series = data.get("Time Series (Daily)", {})
            
            if not time_series:
                return {}
            
            # Filter by date range if provided
            if start_date or end_date:
                filtered_data = {}
                for date_str, values in time_series.items():
                    series_date = date.fromisoformat(date_str)
                    if (start_date is None or series_date >= start_date) and \
                       (end_date is None or series_date <= end_date):
                        filtered_data[date_str] = values
                return filtered_data
            
            return time_series