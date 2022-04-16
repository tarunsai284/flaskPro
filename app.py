from flask import Flask, request, render_template, Response
import constants 
from static.mongoClient import setupMongoClient
from static.cronJob import setupCronJob
import services.cryptoChartService as cryptoChartService

app = Flask(__name__)
app.config.from_object('config')
db = setupMongoClient(app)
collection = db[constants.OHLCV]
setupCronJob(collection)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/mongo')
# def mongo():
#     fromTimeStamp=1609459200000
#     toTimestamp=1640995200000
#     data = mongoLayer.getCrytoDataForTimeRange(collection, "BTC", fromTimeStamp, toTimestamp)
#     return render_template('mongo.html', data=data)

@app.route('/cryptoChart', methods=['GET', 'POST'])   #, methods=['GET', 'POST']
def cryptoChart():
    symbolGet = request.args.get("crypto_select")
    
    graphJSON = {"line": cryptoChartService.plotlyChartService(collection, symbolGet),
                "candle": cryptoChartService.plotlyChartServiceCandle(collection, symbolGet)}
    return render_template('cryptoChart.html', graphJSON=graphJSON)


if __name__ == "__main__":
    print("app")
    app.run()