from pydantic import BaseModel
from typing import Optional


class UpdateCompanyControlRequest(BaseModel):
    status: Optional[str] = None
    ownerUserId: Optional[str] = None