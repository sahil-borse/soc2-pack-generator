from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CreateFrameworkRequest(BaseModel):
    name: str = Field(min_length=2)
    code: str = Field(min_length=2)
    version: Optional[str] = None
    description: Optional[str] = None


class FrameworkResponse(BaseModel):
    id: str
    name: str
    code: str
    version: Optional[str]
    description: Optional[str]
    createdAt: datetime