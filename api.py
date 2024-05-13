from fastapi import APIRouter, Query, HTTPException
from datetime import datetime
from utils import get_adjusted_time

router = APIRouter()


@router.get("/time")
async def get_time(timezone: str = Query(None)):
    current_time = datetime.utcnow().isoformat()
    adjusted_time = None

    if timezone:
        try:
            adjusted_time = get_adjusted_time(timezone)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    return {"currentTime": current_time, "adjustedTime": adjusted_time}
