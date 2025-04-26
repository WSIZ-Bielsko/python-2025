from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette import status

security = HTTPBearer()

# Define the password
PASSWORD = "123"  # Replace with your actual password


# Dependency for password check
async def verify_password(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials
