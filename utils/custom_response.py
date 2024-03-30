from typing import Any, Optional
from pydantic import BaseModel

class CustomResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None
