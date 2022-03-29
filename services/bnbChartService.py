import json, plotly
import static.mongoDBLayer as mongoLayer
import plotly.express as px
import plotly.graph_objects as go
import datetime, time

def plotlyChartService(collection):
    fromTimeStamp=1609459200000
    toTimestamp=1640995200000
    projection = {"timestamp": 1, "close": 1}
    mongoData = mongoLayer.getCrytoDataForTimeRangeProjection(collection, "BNB", fromTimeStamp, toTimestamp, projection)
    
    chartData = {"Date":[], "Closing Price":[]}
    for ele in mongoData:
        dateConv = datetime.date.fromtimestamp((ele.get("timestamp"))/1000)
        chartData["Date"].append(dateConv) #xAxis
        chartData["Closing Price"].append(ele.get("close"))     #yAxis

    fig = px.line(chartData, x='Date', y='Closing Price')

    graphJSONln = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSONln

def plotlyChartServiceCandle(collection):
    fromTimeStamp=1609459200000
    toTimestamp=1640995200000
    projection = {"timestamp": 1, "open": 1, "high": 1, "low": 1, "close": 1}
    mongoData = mongoLayer.getCrytoDataForTimeRangeProjection(collection, "BNB", fromTimeStamp, toTimestamp, projection)
    
    chartData = {"Date":[], "Open":[], "High":[], "Low":[], "Close":[]}
    for ele in mongoData:
        dateConv = datetime.date.fromtimestamp((ele.get("timestamp"))/1000)
        chartData["Date"].append(dateConv)
        chartData["Open"].append(ele.get("open"))
        chartData["High"].append(ele.get("high"))
        chartData["Low"].append(ele.get("low"))
        chartData["Close"].append(ele.get("close"))

    fig = go.Figure(data=[go.Candlestick(x=chartData['Date'], open=chartData['Open'], high=chartData['High'], low=chartData['Low'], close=chartData['Close'])])

    fig.update_layout(
        title="BNB Candlestick",
        yaxis_title="BNB Price"
    )

    graphJSONcndl = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSONcndl