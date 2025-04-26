import mimetypes

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
import os
from pathlib import Path
import shutil

from fastapi.security import HTTPAuthorizationCredentials
from loguru import logger

from python_2025.uploader_app.app_security import verify_password

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "File uploaded successfully"}


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Check if file exists
    if not Path(file_path).is_file():
        raise HTTPException(status_code=404, detail="File not found")

    # Guess the MIME type based on the file extension
    media_type, _ = mimetypes.guess_type(file_path)
    media_type = media_type or "application/octet-stream"  # Fallback to octet-stream if unknown

    logger.info(f'filename = {filename}')
    # Return FileResponse with proper headers
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type=media_type,
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )
@app.get("/list-files/")
async def list_files(credentials: HTTPAuthorizationCredentials = Depends(verify_password)):
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}




if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8001)
