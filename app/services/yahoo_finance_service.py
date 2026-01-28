import yfinance as yf
from fastapi import HTTPException

def fetch_stock_history(ticker: str, period: str):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    
    if df.empty:
        raise HTTPException(status_code=404, detail="No data found")
    
    # Clean up the data
    df.index = df.index.strftime('%Y-%m-%d')
    return df.reset_index().to_dict(orient="records")