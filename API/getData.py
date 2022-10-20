import datetime
import requests

from API.station import Station

url = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json?maxfeatures=-1"


def getData():
    response = requests.get(url)
    return response.json()


def getStations(timestamp=str(datetime.datetime.now)):
    stations = []
    data = getData()
    for el in data["values"]:
        stations.append(Station(el,timestamp=timestamp))
    return stations

if __name__ == "__main__":
    s = getStations()
