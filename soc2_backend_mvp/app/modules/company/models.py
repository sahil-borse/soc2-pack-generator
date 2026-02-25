from pydantic import BaseModel, Field


class CreateCompanyRequest(BaseModel):
    name: str = Field(min_length=2)