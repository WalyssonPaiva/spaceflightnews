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
    if last== None:
        return 1
    return last[0]['id'] + 1

def get_articles(page, per_page):
    collection = connection.get_collection('articles')
    items =  collection.find().sort("_id", -1).skip((page -1)* per_page).limit(per_page)
    response = []
    for item in items:
        del item["_id"]
        response.append(item)
    return response

def get_article(id):
    collection = connection.get_collection('articles')
    item = collection.find_one({"id": id})
    del item["_id"]
    return item

def update_article(id, article):
    collection = connection.get_collection('articles')
    collection.update_one({"id": id}, {"$set": article})
    return article

def delete_article(id):
    collection = connection.get_collection('articles')
    collection.delete_one({"id": id})
    return id

def insert_many(articles):
    collection = connection.get_collection('articles')
    collection.insert_many(articles)

def get_by_title(title):
    collection = connection.get_collection('articles')
    item = collection.find_one({"title": title})
    if item:
        del item["_id"]
        return item
    return None