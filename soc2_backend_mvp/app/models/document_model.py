from pydantic import BaseModel, Field
from datetime import datetime


class DocumentPublic(BaseModel):
    id: str
    policyKey: str
    title: str
    contentMarkdown: str
    createdAt: datetime
    updatedAt: datetime


class DocumentUpdate(BaseModel):
    contentMarkdown: str = Field(min_length=20)
