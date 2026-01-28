from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.api import stocks
from app.utils.limiter import limiter


# 1. Initialize the limiter (identifies users by their IP address)
app = FastAPI(title="Stock History API")

# 2. Add the limiter to the app state and set up the error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(stocks.router, prefix="/stocks", tags=["stocks"])

@app.get("/")
@limiter.limit("1/second")
async def health_check(request: Request):
    return {"status": "healthy"}