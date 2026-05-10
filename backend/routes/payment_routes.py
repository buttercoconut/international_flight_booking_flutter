from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/process")
async def process_payment(booking_id: str, amount: float):
    # Dummy payment processing
    return {"booking_id": booking_id, "status": "paid", "amount": amount}
