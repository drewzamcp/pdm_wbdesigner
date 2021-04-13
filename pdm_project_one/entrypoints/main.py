import fastapi
import fastapi_chameleon
import uvicorn

from pdm_project_one.settings import TEMPLATE_FLDR

from pdm_project_one import views

app = fastapi.FastAPI()


def main():
    uvicorn.run(app)
    configure()


def configure():
    configure_templates()
    configure_routes()


def configure_routes():
    app.include_router(views.home.router)
    app.include_router(views.designer.router)


def configure_templates():
    fastapi_chameleon.global_init(f"{TEMPLATE_FLDR}")


if __name__ == "__main__":
    main()
