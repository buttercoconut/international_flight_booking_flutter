from fastapi import APIRouter, Depends, HTTPException
from typing import Dict

router = APIRouter()

# Dummy payment endpoint
@router.post("/process")
async def process_payment(data: Dict):
    # In a real system, integrate with a payment gateway
    return {"status": "success", "transaction_id": "TXN123456"}
