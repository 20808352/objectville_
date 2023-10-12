import flask
from flask import request
from SubwayLoader import SubwayLoader

app = flask.Flask(__name__)
app.config["DEBUG"] = True

subway = []
    
@app.route('/checkStationExist', methods=['GET'])
def checkStationExist():
    json = request.json
    stationName = json["StationName"]

    has_station = subway.has_station(stationName)
    
    if (has_station == True):
        return (f"Station {stationName} exists", 200)
    return (f"Station {stationName} does not exists", 404)
    
@app.route('/addStation', methods=['POST'])
def addStation():
    json = request.json
    stationName = json["StationName"]

    result = subway.add_station(stationName)
    
    if (result == True):
        return (f"Station {stationName} already exists", 200)
    return (f"Station {stationName} added", 201)

@app.route('/checkConnectionExists', methods=['GET'])
def checkConnectionExists():
    json = request.json
    stationName1 = json["StationName1"]
    stationName2 = json["StationName2"]
    line = json["Line"]

    result = subway.has_connection(stationName1, stationName2, line)
    
    if (result != None):
        return (f"{result}", 200)
    return ("Connection does not exists", 404)

@app.route('/addConnection', methods=['POST'])
def addConnection():
    json = request.json
    stationName1 = json["StationName1"]
    stationName2 = json["StationName2"]
    line = json["Line"]

    result = subway.add_connection(stationName1, stationName2, line)
    
    if (result == True):
        return (f"Connection between {stationName1} & {stationName2} added", 201)
    return ("Connection does not exists", 404)

@app.route('/getDirections', methods=['GET'])
def getDirections():
    json = request.json
    stationName1 = json["StationName1"]
    stationName2 = json["StationName2"]

    result = subway.get_directions(stationName1, stationName2)
    
    if (result == False):
        return (f"Either station {stationName1} or {stationName2} does not exist", 404)
    return (result, 200)

@app.route('/getConnection', methods=['GET'])
def getConnection():
    json = request.json
    stationName1 = json["StationName2"]
    stationName2 = json["StationName1"]
    
    connection = subway.get_connection(stationName1, stationName2)
    
    if (connection != None):
        return (f"{connection}", 200)
    return ("Connection does not exists", 404)

@app.route('/addToNetwork', methods=['POST'])
def addToNetwork():
    json = request.json
    stationName1 = json["StationName2"]
    stationName2 = json["StationName1"]
    
    subway.get_connection(stationName1, stationName2)
    
    return ("Success", 200)

if __name__ == '__main__':
    loader = SubwayLoader()
    loader.loadFromFile("ObjectvilleSubway.txt")
    subway = loader.get_subway()

app.run()