def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://root:docker@localhost"
    client = MongoClient(CONNECTION_STRING)
    return client['spaceflightnews']

def get_collection(collection_name):
    return get_database()[collection_name]
