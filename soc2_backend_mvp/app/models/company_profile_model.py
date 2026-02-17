from pydantic import BaseModel, Field
from typing import Any, Dict


class CompanyProfileUpsert(BaseModel):
    profile: Dict[str, Any] = Field(default_factory=dict)


class CompanyProfilePublic(BaseModel):
    id: str
    userId: str
    profile: Dict[str, Any]
