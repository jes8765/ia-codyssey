from pydantic import BaseModel


class DataCreate(BaseModel):
    date: str
    value: float
    volume: int
    open: float
    high: float
    low: float
    memo: str = ""


class DataResponse(DataCreate):
    id: str