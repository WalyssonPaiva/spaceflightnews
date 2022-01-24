from fastapi import Depends, FastAPI, HTTPException
from services import article as s_article


app = FastAPI()
app.include_router(s_article.router)

@app.get("/", status_code=200)
async def root():
    return "Back-end Challenge 2021 🏅 - Space Flight News"

