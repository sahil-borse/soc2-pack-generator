from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CreateControlRequest(BaseModel):
    frameworkId: str
    controlCode: str = Field(min_length=2)
    title: str = Field(min_length=2)
    category: Optional[str] = None
    description: Optional[str] = None
    defaultReviewFrequency: Optional[str] = None


class ControlResponse(BaseModel):
    id: str
    frameworkId: str
    controlCode: str
    title: str
    category: Optional[str]
    description: Optional[str]
    defaultReviewFrequency: Optional[str]
    createdAt: datetime