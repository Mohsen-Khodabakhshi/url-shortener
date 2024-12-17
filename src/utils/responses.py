from pydantic import BaseModel

from typing import Any


class ResponseStructure(BaseModel):
    details: Any
    status_code: int
