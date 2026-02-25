from pydantic import BaseModel
from typing import List


class BoardColumn(BaseModel):
    key: str
    label: str
    order: int


class UpdateBoardConfigRequest(BaseModel):
    frameworkId: str
    columns: List[BoardColumn]