from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    transaction_id: str
    source_account: str
    destination_account: str
    amount: float
    currency: str

class TransactionRead(TransactionCreate):
    status: str
    created_at: datetime
    processed_at: datetime | None = None

    class Config:
        from_attributes = True
