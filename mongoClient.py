from flask_pymongo import PyMongo
import constants

def setupMongoClient(app):
    mongodb_client = PyMongo(app)
    db = mongodb_client.db
    if "OHLCV" not in  db.list_collection_names():
        db.create_collection("OHLCV")
        print("Collection created")
    
    # Sample CRUD
    # ohlcvCollection = db[constants.OHLCV]
    # ohlcvCollection.insert_one({'title': "todo title", 'body': "todo body"})
    # ohlcvCollection.delete_many({})
    
    return db