"""FastAPI router for payment processing (stub)."""

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/process")
async def process_payment():
    # Stub: In real implementation, integrate with payment gateway
    return {"status": "success", "transaction_id": "txn_123456"}
