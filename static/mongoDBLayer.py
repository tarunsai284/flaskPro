import logging
from flask_pymongo import pymongo, PyMongo
from string_utils import *
import constants, time
import logging

# write your database CRUD functions here 
# We have indexed the file according to timestamp and symbol, CRUD operations will be faster on these fields
# Please be carefull of updating data. 

logger = logging.getLogger("monogDBLayer")

def getCrytoDataForTimeRange(collection, symbol=None, fromTimeStamp=None, toTimestamp=None, sortTimestamp=pymongo.ASCENDING):
    query={}
    result={}
    try: 
        if(collection==None): raise ValueError("Collection cannont be null")
        if(is_full_string(symbol)): query["symbol"] = symbol

        if(toTimestamp==None): toTimestamp = int(time.time()*1000)
        if(fromTimeStamp==None): fromTimeStamp = toTimestamp-31536000000

        query["timestamp"] = { "$gte": fromTimeStamp, "$lte": toTimestamp }
        print("query: {}".format(query))

        if(sortTimestamp!=pymongo.ASCENDING): 
            result = collection.find(query).sort("timestamp",sortTimestamp)
        else: result = collection.find(query)

    except ValueError as e: 
        print(e)
    except Exception as e:
        print(e)

    return result
