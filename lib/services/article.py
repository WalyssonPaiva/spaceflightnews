from fastapi import APIRouter
from database import article as article_db
from models.article import Article

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    responses={403: {"description": "Forbidden"}},
)

@router.post("/")
async def create_article(article: Article):
    article.id = article_db.get_next_id()
    article_db.create_article(article.dict())
    return article

