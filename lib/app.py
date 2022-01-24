from fastapi import Depends, FastAPI, HTTPException
from services import article as s_article
import update_db_cron
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
app.include_router(s_article.router)

@app.get("/", status_code=200)
async def root():
    return "Back-end Challenge 2021 🏅 - Space Flight News"


@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_db_cron.update_db, 'cron', hour=12, minute=55, second=0)
    scheduler.start()



