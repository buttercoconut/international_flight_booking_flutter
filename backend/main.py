from fastapi import FastAPI
from routes.flight_routes import router as flight_router

app = FastAPI(title="International Flight Booking API")

app.include_router(flight_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
