from functools import wraps
from ..utils.response import sendResponse

def asyncHandler(func):
    @wraps(func)  # Ensures the original function name is preserved
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return sendResponse(status="error", message="An unexpected error occurred.", error=str(e))
    return wrapper