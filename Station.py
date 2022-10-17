class Station:
    def __init__(self,rep):
        self.name = rep.get("name")
        self.coord = {"lat": rep.get("lat"), "long": rep.get("lng")}
        self.bikes = {"available": rep.get("available_bikes"), "stands": rep.get("available_bike_stands")}

    def __str__(self) -> str:
        return self.name

    