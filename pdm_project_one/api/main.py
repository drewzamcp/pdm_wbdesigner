import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from pdm_project_one.settings import TEMPLATE_FLDR, STATIC_FLDR
from pdm_project_one.api.views import router

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, debug=True)


def configure():
    app.mount("/static", StaticFiles(directory=STATIC_FLDR), name="static")
    configure_routes()
    configure_templates()


def configure_routes():
    app.include_router(router)


def configure_templates():
    fastapi_chameleon.global_init(f"{TEMPLATE_FLDR}")


if __name__ == "__main__":
    main()
