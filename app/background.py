import time
from sqlalchemy.orm import Session
from .crud import mark_processed

def process_transaction(transaction_id: str, db: Session):
    time.sleep(30)  # simulate delay
    mark_processed(db, transaction_id)
