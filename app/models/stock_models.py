from pydantic import BaseModel

class StockPrice(BaseModel):
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: int

class StockResponse(BaseModel):
    symbol: str
    period: str
    history: list[StockPrice]