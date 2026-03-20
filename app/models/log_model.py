# Here I will implement the LogModel class which will be responsible for handling log data and providing methods to analyze it.
from pydantic import BaseModel
from typing import Optional

class LogModel(BaseModel):
    record_id: int
    ip: str
    timestamp: str
    method: str
    endpoint: str
    protocol: str
    status_code: int
    response_size: int
    referrer: Optional[str] = None
    user_agent: Optional[str] = None
    extra_field: Optional[str] = None