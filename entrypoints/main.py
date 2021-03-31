import fastapi
import fastapi_chameleon
import uvicorn
from pdm_project_one.settings import TEMPLATE_FLDR

from views import account, designer, home

app = fastapi.FastAPI()


def main():
    uvicorn.run(app)


def configure():
    configure_templates()
    configure_routes()


def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(designer.router)


def configure_templates():
    fastapi_chameleon.global_init(f"{TEMPLATE_FLDR}")


if __name__ == "__main__":
    main()
else:
    configure()
