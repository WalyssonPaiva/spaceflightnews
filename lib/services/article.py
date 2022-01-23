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

@router.get("/")
async def get_articles(page: int, per_page: int):
    return article_db.get_articles(page, per_page)

@router.get("/{id}")
async def get_article(id: int):
    return article_db.get_article(id)

@router.put("/{id}")
async def update_article(id: int, article: Article):
    article.id = id
    article_db.update_article(id, article.dict())
    return article

@router.delete("/{id}")
async def delete_article(id: int):
    article_db.delete_article(id)
    return {"id": id}

