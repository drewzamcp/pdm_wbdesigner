import os
import shutil

import fastapi
from fastapi import APIRouter, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi_chameleon import template
from starlette.requests import Request
from starlette import status

from pdm_project_one.api.viewmodels import DesignViewModel
from pdm_project_one.library import imguploads
from pdm_project_one.settings import UPLOADS_FLDR

router = APIRouter()


@router.get("/")
@template(template_file="home/index.pt")
def index(user: str = "anon"):
    return {"user_name": user}


@router.get("/designer")
@template(template_file="designer/designer.pt")
def designer(request: Request):
    vm = DesignViewModel(request)
    return vm.to_dict()


@router.post("/designer/upload")
@template(template_file="designer/output.pt")
def designer(request: Request):
    vm = DesignViewModel(request)
    vm.load()

    if vm.error:
        return vm.to_dict()

    tmp_file_path = imguploads.save_upload_file_tmp(vm.final_image)
    print(tmp_file_path)
    # artwork = create_artwork(vm.final_text, tmp_file_path)

    resp = fastapi.responses.FileResponse(tmp_file_path)

    return resp


@router.post("/files/upload")
def create_file(file: UploadFile = File(...)):
    file_object = file.file
    # create empty file to copy the file_object to
    upload_folder = open(os.path.join(UPLOADS_FLDR, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    return {"filename": file.filename}

# @router.post("/designer/new", response_class=HTMLResponse)
# @template(template_file="designer/output.pt")
# def designer_output(file: File(...), text: str = Form(...)):
#     return {"file": file, "text": text}
