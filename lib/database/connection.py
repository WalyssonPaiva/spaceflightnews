def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://root:docker@localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client['spaceflightnews']

def get_collection(collection_name):
    return get_database()[collection_name]
