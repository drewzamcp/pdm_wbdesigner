import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/account")
def account():
    return {}
