
import datetime
from sqlite3 import Timestamp
from time import time


class Station:
    def __init__(self,rep,timestamp=datetime.datetime.now()):
        self.timestamp = timestamp
        self.id = rep.get("number")
        self.commune = rep.get("commune")
        self.name = rep.get("name")
        self.address = rep.get("address")
        self.lat = rep.get("lat",'erreur')
        self.lng = rep.get("lng",'erreur')
        self.available_bikes = rep.get("available_bikes")
        self.available_bike_stands = rep.get("available_bike_stands")
    
    def __str__(self) -> str:
        return self.name

    def json(self,init=False):
        if init: return {
            "id":self.id,
            "name":self.name,
            "address":self.address,
            "commune":self.commune,
            "lat":self.lat,
            "lng":self.lng
        }
        return {
            "id":self.id,
            "available_bikes": self.available_bikes,
            "available_bike_stands": self.available_bike_stands,
            "timestamp": str(self.timestamp)
        }