import mimetypes
from datetime import datetime
from uuid import uuid4, UUID

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
import os
from pathlib import Path
import shutil

from fastapi.security import HTTPAuthorizationCredentials
from loguru import logger

from python_2025.uploader_app.app_security import verify_password
from python_2025.uploader_app.file_tools import FileMeta, get_meta_by_file_id, get_all_files, validate_file_name

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid4())

    # file will be saved in 2 files; .body contains content, .meta contains information about the file
    body_file_name = file_id + '.body'
    meta_file_name = file_id + '.meta'

    # validate file name
    file_name = validate_file_name(file.filename)

    logger.info(f'saving file {file_name} to {body_file_name}')

    body_file_path = os.path.join(UPLOAD_DIR, body_file_name)

    # Save uploaded file
    with open(body_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_size_mb = int(os.path.getsize(body_file_path) / (1024 * 1024))

    # Save meta file
    meta = FileMeta(file_id=UUID(file_id),
                    original_file_name=file_name,
                    user_id=1,
                    category_id=1,
                    size_mb=file_size_mb,
                    upload_date=datetime.now())
    meta_file_path = os.path.join(UPLOAD_DIR, meta_file_name)
    with open(meta_file_path, 'w') as f:
        f.write(meta.model_dump_json())

    return {"filename": file.filename, "message": "File uploaded successfully"}


@app.get("/download/{file_id}")
async def download_file(file_id: str):
    body_file_name = file_id + '.body'

    meta = get_meta_by_file_id(UUID(file_id))

    file_path = os.path.join(UPLOAD_DIR, body_file_name)

    # Check if file exists
    if not Path(file_path).is_file():
        raise HTTPException(status_code=404, detail="File not found")

    # Guess the MIME type based on the file extension
    media_type, _ = mimetypes.guess_type(file_path)
    media_type = media_type or "application/octet-stream"  # Fallback to octet-stream if unknown

    # file_id = 'cv.pdf'
    # final_file_name = 'aaa.png'

    # Return FileResponse with proper headers
    return FileResponse(
        path=file_path,
        filename=meta.original_file_name,
        media_type=media_type,
        headers={
            "Content-Disposition": f"attachment; filename={meta.original_file_name}"
        }
    )


@app.get("/list-files/")
async def list_files(credentials: HTTPAuthorizationCredentials = Depends(verify_password)):
    # files = os.listdir(UPLOAD_DIR)
    return {"files": get_all_files()}


@app.get("/date/")
async def get_current_server_date():
    logger.info('checking server time')
    current_date = str(datetime.now())
    return {"current server date": current_date}


# potrzebne biblioteki: fastapi, uvicorn, python-multipart, loguru, pydantic
if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8001)
