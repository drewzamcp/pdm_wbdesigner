import fastapi
from fastapi import UploadFile, File
import shutil
from fastapi_chameleon import template

from settings import UPLOADS_FLDR

router = fastapi.APIRouter()


@router.get("/")
@template(template_file="home/index.pt")
def index(user: str = "anon"):
    return {"user_name": user}


@router.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"{UPLOADS_FLDR}/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
