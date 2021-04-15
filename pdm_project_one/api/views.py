from fastapi import APIRouter, File, UploadFile, Form
from pydantic import BaseModel
from fastapi_chameleon import template

from pdm_project_one.program.program import create_artwork


router = APIRouter()


class ImageFile(BaseModel):
    file: UploadFile = File(...)


@router.get("/")
@template(template_file="home/index.pt")
def index(user: str = "anon"):
    return {"user_name": user}


@router.get("/designer")
@template(template_file="designer/designer.pt")
def designer():
    return {}


@router.post("/designer/output")
@template(template_file="designer/output.pt")
def designer_output(file: ImageFile, text: str = ""):
    artwork = create_artwork(file, text)
    return artwork
