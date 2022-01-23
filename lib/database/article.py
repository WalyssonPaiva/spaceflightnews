from . import connection

def create_article(article):
    collection = connection.get_collection('articles')
    collection.insert_one(article)
    return article

def get_latest():
    collection = connection.get_collection('articles')
    return collection.find().sort("_id", -1).limit(1)

def get_next_id():
    last = get_latest()
    return last[0]['id'] + 1