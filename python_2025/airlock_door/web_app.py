from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from door import Door, DoorError

app = FastAPI(title="Door Control API", description="API for managing airlock door operations")

# Global door instance
door = Door()

"""
Generated with AI (Claude 4) with

create app.py with full api using fastapi library 
and providing access to all methods of Door class

{contents of door.py}

"""


# Pydantic models for request/response
class EnterRequest(BaseModel):
    occupant: str
    direction: str


class LeaveRequest(BaseModel):
    occupant: str
    direction: str


class DoorStatus(BaseModel):
    air_lock_occupant: str | None
    current_occupants: List[str]


class OperationResponse(BaseModel):
    success: bool
    message: str


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {"message": "Door Control API", "version": "1.0.0"}


@app.get("/status", response_model=DoorStatus)
async def get_door_status():
    """Get current door status including airlock occupant and current occupants"""
    return DoorStatus(
        air_lock_occupant=door.air_lock_occupant,
        current_occupants=door.current_room_occupants
    )


@app.post("/enter", response_model=OperationResponse)
async def enter_door(request: EnterRequest):
    """Enter the airlock"""
    try:
        door.enter_airlock(request.occupant, request.direction)
        return OperationResponse(
            success=True,
            message=f"{request.occupant} successfully entered the airlock"
        )
    except DoorError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.post("/leave", response_model=OperationResponse)
async def leave_door(request: LeaveRequest):
    """Leave the airlock"""
    try:
        door.leave_airlock(request.occupant, request.direction)
        return OperationResponse(
            success=True,
            message=f"{request.occupant} successfully left the airlock"
        )
    except DoorError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/airlock-occupant")
async def get_airlock_occupant():
    """Get current airlock occupant"""
    return {"air_lock_occupant": door.air_lock_occupant}


@app.get("/current-occupants")
async def get_current_occupants():
    """Get list of current occupants"""
    return {"current_occupants": door.current_room_occupants}


@app.post("/reset")
async def reset_door():
    """Reset door state (clear airlock and occupants)"""
    door.air_lock_occupant = None
    door.current_room_occupants = []
    return OperationResponse(
        success=True,
        message="Door state has been reset"
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
