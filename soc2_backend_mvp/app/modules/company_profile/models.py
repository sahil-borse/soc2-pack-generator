from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class CreateCompanyRequest(BaseModel):
    name: str = Field(min_length=2, max_length=200)


class CompanyResponse(BaseModel):
    id: str
    name: str
    role: Optional[str] = None
    createdAt: datetime
