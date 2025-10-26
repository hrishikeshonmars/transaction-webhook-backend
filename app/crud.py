from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas

def get_transaction(db: Session, transaction_id: str):
    return db.query(models.Transaction).filter(models.Transaction.transaction_id == transaction_id).first()

def create_transaction(db: Session, txn: schemas.TransactionCreate):
    db_txn = models.Transaction(**txn.dict())
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn

def mark_processed(db: Session, transaction_id: str):
    txn = get_transaction(db, transaction_id)
    if txn and txn.status != "PROCESSED":
        txn.status = "PROCESSED"
        txn.processed_at = datetime.utcnow()
        db.commit()
        db.refresh(txn)
    return txn
