import os
from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv

load_dotenv()

# We tell FastAPI to look for 'X-API-KEY' in the request headers
API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Get the secret from environment variables
EXPECTED_API_KEY = os.getenv("API_KEY")
print(f"Expected API Key: {EXPECTED_API_KEY}")  # For debugging purposes; remove in production

async def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key == EXPECTED_API_KEY:
        return api_key
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid or missing API Key",
    )