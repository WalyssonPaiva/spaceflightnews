from fastapi import APIRouter

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    responses={403: {"description": "Forbidden"}},
)
