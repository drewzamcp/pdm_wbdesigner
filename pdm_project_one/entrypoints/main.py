import fastapi
import fastapi_chameleon
import uvicorn
from fastapi.staticfiles import StaticFiles

from pdm_project_one.settings import TEMPLATE_FLDR, STATIC_FLDR

from views import home, designer

app = fastapi.FastAPI()
# app.mount(STATIC_FLDR, StaticFiles(directory="static"), name="static")


def main():
    configure()
    uvicorn.run(app)


def configure():
    configure_routes()
    configure_templates()


def configure_routes():
    app.include_router(home.router)
    app.include_router(designer.router)


def configure_templates():
    fastapi_chameleon.global_init(f"{TEMPLATE_FLDR}")


if __name__ == "__main__":
    main()
