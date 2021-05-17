import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from pdm_project_one.settings import TEMPLATE_FLDR, STATIC_FLDR
from pdm_project_one.api.views import router

app = fastapi.FastAPI()


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()


def configure_templates(dev_mode: bool):
    fastapi_chameleon.global_init(f"{TEMPLATE_FLDR}")


def configure_routes():
    # TODO: could use Mike's decorator package fastapi_chameleon
    app.mount("/static", StaticFiles(directory=STATIC_FLDR), name="static")
    app.include_router(router)


if __name__ == "__main__":
    main()
