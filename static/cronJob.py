import constants, requests, atexit
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import static.mongoDBLayer as mongoLayer

collection = None

def setupCronJob(coll):
    collection = coll
    try: 
        if(collection==None): raise ValueError("Collection cannont be null")
        sched = BackgroundScheduler(daemon=True)
        sched.add_job(func=updateDatabase,trigger='interval',args=[collection], days=1)
        sched.start()

        atexit.register(lambda: sched.shutdown())
    except Exception as e:
        print(e)
    

def updateDatabase(collection):
    candleData = {}
    cryptoList = []

    today = datetime.now()
    # today = datetime(2022, 3, 1)

    before = today - timedelta(days = 1)
    after = today - timedelta(days = 2)
    beforeStamp = int(before.timestamp())
    afterStamp = int(after.timestamp())

    # Fetch Data
    query = {"after":afterStamp, "before":beforeStamp, "periods": [86400]}
    # Each candle is a list of [close_timestamp, open, high, low, close, volume, volume_quote]
    ohlcPaths = ["btcusdt", "ethusdt", "ltcusdt", "neousdt", "bnbusdt"]

    try:
        for pair in ohlcPaths:
            url = constants.CRYPTOWATCH_OHLCV.format(pair)
            response = requests.get(url, params=query)
            if not response.ok: raise ValueError("!!!!! cryptowatch api call was not successfull")
            data = response.json()["result"]["86400"]
            if not data: raise ValueError("cryptoList cannot be empty")
            candleData[pair] =  data

        for pair in candleData:
            symbol = pair[:-len("pair")]
            # the each candle stick data point. 
            for dataPoint in candleData.get(pair):
                map = {} 
                timestamp = dataPoint[0]
                map["timestamp"] = timestamp*1000
                map["date"] = datetime.utcfromtimestamp(timestamp)
                map["symbol"] = symbol
                map["open"] = dataPoint[1]
                map["high"] = dataPoint[2]
                map["low"] = dataPoint[3]
                map["close"] = dataPoint[4]
                map["VolumeBTC"] = dataPoint[5]
                map["VolumeUSDT"] = dataPoint[6]
                cryptoList.append(map)


        # Update crypto data to mongoDb    
        mongoLayer.dailyUpdate(collection, cryptoList)
    except Exception as e:
        print(e)
        

        