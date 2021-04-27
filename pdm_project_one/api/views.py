import fastapi
from fastapi import APIRouter, Form, File
from fastapi.responses import FileResponse
from fastapi_chameleon import template

from starlette.requests import Request

# from pdm_project_one.library.program import create_artwork
from pdm_project_one.api.viewmodels import DesignViewModel
from pdm_project_one.library.program import create_artwork
from pdm_project_one.library.imgtools import save_upload_file_tmp
from pdm_project_one.settings import IMG_OUTPUT_FLDR

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


@router.post("/designer/output")
@template(template_file="designer/output.pt")
async def designer(request: Request):
    vm = DesignViewModel(request)
    await vm.load()

    save_img = save_upload_file_tmp(vm.final_image)
    wb_text = vm.final_text

    artwork = create_artwork(wb_text, save_img)
    output_img = f"{IMG_OUTPUT_FLDR}/tmp_joined.png"

    return FileResponse(output_img)
