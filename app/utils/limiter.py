from slowapi import Limiter
from slowapi.util import get_remote_address

# This instance is now the "single source of truth"
limiter = Limiter(key_func=get_remote_address)