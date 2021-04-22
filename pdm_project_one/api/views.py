import fastapi
from fastapi import APIRouter, Form, File
from fastapi.responses import HTMLResponse
from fastapi_chameleon import template

from starlette.requests import Request

# from pdm_project_one.library.program import create_artwork
from pdm_project_one.api.viewmodels import DesignViewModel
from pdm_project_one.library.program import create_artwork

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


@router.post("/designer")
@template()
async def designer(request: Request):
    vm = DesignViewModel(request)
    await vm.load()

    artwork = create_artwork(vm.final_text, vm.final_image)

    resp = fastapi.responses.FileResponse(artwork)

    return resp


# @router.post("/designer/new", response_class=HTMLResponse)
# @template(template_file="designer/output.pt")
# def designer_output(file: File(...), text: str = Form(...)):
#     return {"file": file, "text": text}
