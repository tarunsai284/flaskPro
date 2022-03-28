import json, plotly
import static.mongoDBLayer as mongoLayer
import plotly.express as px

def plotlyChartService(collection):
    fromTimeStamp=1609459200000
    toTimestamp=1640995200000
    projection = {"timestamp": 1, "close": 1}
    mongoData = mongoLayer.getCrytoDataForTimeRangeProjection(collection, "BTC", fromTimeStamp, toTimestamp, projection)
    
    chartData = {"xAxis":[], "yAxis":[]}
    for ele in mongoData:
        chartData["xAxis"].append(ele.get("timestamp"))
        chartData["yAxis"].append(ele.get("close"))

    print(chartData)
    fig = px.line(chartData, x='xAxis', y='yAxis')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON