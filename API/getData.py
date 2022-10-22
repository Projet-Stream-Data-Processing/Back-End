import datetime
import requests

from API.station import Station

url = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json?maxfeatures=-1"


def get_data():
    response = requests.get(url)
    return response.json()


def getStations(timestamp=str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))):
    stations = []
    data = get_data()
    for el in data["values"]:
        stations.append(Station(el,timestamp=timestamp))
    return stations

if __name__ == "__main__":
    s = getStations()
