from decouple import config

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = config("DATABASE_CONNECTION")
    client = MongoClient(CONNECTION_STRING)
    return client['spaceflightnews']

def get_collection(collection_name):
    return get_database()[collection_name]
