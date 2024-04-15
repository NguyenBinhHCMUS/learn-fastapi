from typing import Annotated

from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()


@router.post("/file")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@router.post("/file/form-file")
async def create_file_and_form(
        file: Annotated[bytes, File(description="A file read as bytes")],
        fileb: Annotated[UploadFile, File(description="A file read as UploadFile")],
        token: Annotated[str, Form()]
):
    if not file:
        return {"message": "No file sent"}
    else:
        return {
            "file_size": len(file),
            "token": token,
            "fileb_content_type": fileb.content_type,
        }


@router.post("/file/multiple")
async def create_files(files: Annotated[list[bytes], File(description="Multiple files as bytes")]):
    if not files:
        return {"message": "No file sent"}
    else:
        return {"file_size": [len(file) for file in files]}


@router.post("/single")
async def upload(file: Annotated[UploadFile, File(description="A file read as UploadFile")]):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


@router.post("/multiple")
async def upload_multiple(files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")]):
    if not files:
        return {"message": "No upload file sent"}
    else:
        return {"filename": [file.filename for file in files]}
