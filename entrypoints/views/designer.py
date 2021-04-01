import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/designer")
def designer():
    return {}
