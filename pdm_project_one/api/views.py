import fastapi
from fastapi import APIRouter, Form, File
from fastapi.responses import HTMLResponse
from fastapi_chameleon import template
from starlette.requests import Request
from starlette import status

from pdm_project_one.api.viewmodels import DesignViewModel
from pdm_project_one.library import imguploads

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

    resp = fastapi.responses.RedirectResponse('/designer/upload', status_code=status.HTTP_302_FOUND)

    return resp


@router.post("/designer/new", response_class=HTMLResponse)
@template(template_file="designer/output.pt")
def designer_output(file: File(...), text: str = Form(...)):
    return {"file": file, "text": text}
