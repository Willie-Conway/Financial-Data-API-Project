# Financial-Data-API-Project\populate_stocks.py
import yfinance as yf
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base  # your SQLAlchemy base
from app.models import FinancialData  # your ORM model class for financial_data

# Your database URL (update with your actual credentials)
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/financial_data"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# List of stock symbols you want real data for
symbols = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
    "FB", "NVDA", "JPM", "V", "JNJ",
    "WMT", "PG", "MA", "DIS", "HD",
    "BAC", "ADBE", "NFLX", "PYPL", "CMCSA",
    "XOM", "KO", "PFE", "MRK", "PEP",
    "CSCO", "T", "INTC", "VZ", "CVX",
    "ORCL", "ABT", "CRM", "COST", "MCD",
    "NKE", "MDT", "IBM", "TXN", "UNH",
    "QCOM", "LOW", "LIN", "BMY", "GE",
    "AMGN", "MMM", "UPS", "BA", "CAT"
]


# Fetch today's date
today = datetime.date.today()

for symbol in symbols:
    # Download stock data for today
    data = yf.download(symbol, start=today, end=today + datetime.timedelta(days=1))

    if not data.empty:
        open_price = data['Open'][0]
        close_price = data['Close'][0]
        volume = int(data['Volume'][0])

        # Create your ORM object
        stock_entry = FinancialData(
            symbol=symbol,
            date=today,
            open_price=open_price,
            close_price=close_price,
            volume=volume
        )
        
        session.add(stock_entry)
        print(f"Added {symbol}: Open={open_price}, Close={close_price}, Volume={volume}")
    else:
        print(f"No data for {symbol} on {today}")

# Commit all additions to DB
session.commit()
session.close()
