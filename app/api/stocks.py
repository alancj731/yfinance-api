from fastapi import APIRouter, Query, Request
from app.services.yahoo_finance_service import fetch_stock_history
from app.models.stock_models import StockResponse
from app.utils.limiter import limiter

router = APIRouter()

@router.get("/{ticker}", response_model=StockResponse)
@limiter.limit("1/second")
async def get_stock(request: Request, ticker: str, period: str = Query("5y", regex="^(1d|5d|1mo|1y|5y|max)$")):
    data = fetch_stock_history(ticker.upper(), period)
    return {
        "symbol": ticker.upper(),
        "period": period,
        "history": data
    }