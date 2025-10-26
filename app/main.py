from fastapi import FastAPI, BackgroundTasks, Depends, status
from sqlalchemy.orm import Session
from datetime import datetime
from . import schemas, crud, models, database
from .background import process_transaction

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health_check():
    return {"status": "HEALTHY", "current_time": datetime.utcnow().isoformat()}

@app.post("/v1/webhooks/transactions", status_code=status.HTTP_202_ACCEPTED)
def receive_webhook(txn: schemas.TransactionCreate, background: BackgroundTasks, db: Session = Depends(get_db)):
    existing = crud.get_transaction(db, txn.transaction_id)
    if not existing:
        crud.create_transaction(db, txn)
        background.add_task(process_transaction, txn.transaction_id, db)
    return {"message": "Webhook received"}

@app.get("/v1/transactions/{transaction_id}", response_model=schemas.TransactionRead)
def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    txn = crud.get_transaction(db, transaction_id)
    if not txn:
        return {"error": "Not found"}
    return txn
