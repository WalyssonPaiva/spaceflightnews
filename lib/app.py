from fastapi import Depends, FastAPI, HTTPException
from services import article as s_article


app = FastAPI()
app.include_router(s_article.router)



