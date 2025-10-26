📘 Backend — README.md
# 🧠 Transaction Webhook Processor (FastAPI)

## Overview
A background-processing service that handles payment transaction webhooks asynchronously.  
The service acknowledges webhooks instantly (within 500 ms) and processes them in the background with a simulated delay.

---

## 🧩 Features
- Built with **FastAPI**
- **Webhook endpoint** for receiving transactions
- **Health check** endpoint
- **Idempotent** transaction handling (duplicate-safe)
- **Asynchronous background processing**
- **Persistent SQLite storage**
- Responds with **202 Accepted** instantly while continuing work in the background

---

## ⚙️ API Endpoints

### `GET /`
Health check
```json
{
  "status": "HEALTHY",
  "current_time": "2025-10-26T10:30:00Z"
}
```
### POST /v1/webhooks/transactions

Receives webhook payload.
Example:
```
{
  "transaction_id": "txn_abc123",
  "source_account": "acc_user_789",
  "destination_account": "acc_merchant_456",
  "amount": 1500,
  "currency": "INR"
}
```

Response:
```
{"message": "Webhook received"}
```

(returns 202 immediately)

### GET /v1/transactions/{transaction_id}

Retrieve transaction status and timing.
Example Response:
```
{
  "transaction_id": "txn_abc123",
  "status": "PROCESSED",
  "created_at": "...",
  "processed_at": "..."
}
```
## 🧠 Tech Stack

Python 3.12  

FastAPI 0.120.0  

SQLAlchemy 2.0  

Pydantic v2  

SQLite (for persistence)  

## ▶️ Run Locally
git clone https://github.com/hrishikeshonmars/transaction-webhook-backend  
cd transaction-webhook-backend  
pip install -r requirements.txt  
uvicorn app.main:app --reload  


Then visit: http://127.0.0.1:8000  

## ☁️ Deployed API  

Live URL:  
🔗 https://transaction-webhook-backend-2.onrender.com/  
