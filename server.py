import random
import json
from pymongo import MongoClient
from paho.mqtt import client as mqtt_client
from mqtt import connect_mqtt

mongoUser="user"
mongoPass="password"
mongoClient = MongoClient(f"mongodb://{mongoUser}:{mongoPass}@localhost:27017")

def subscribe(client: mqtt_client,topic):
    def on_message(client, userdata, msg):
        message = json.loads(str(msg.payload.decode()))
        
        print(f"`{msg.topic}` - ",end="")
        
        
        if msg.topic == "getStation":
            saveStationToDatabase(message)

        elif msg.topic == "getStationName":
            save_name_to_database(message)
        print("db ok")

    client.subscribe(topic)
    client.on_message = on_message
    

def save_name_to_database(data):
    # Set up client for MongoDB
    
    db=mongoClient.Velov
    c_StationName=db.StationName
    
    c_StationName.find_one_and_update(
        {"name":data.get("name")},
        {"$set":
            {
                "id":data.get("id"),
                "address":data.get("address"),
                "commune":data.get("commune"),
                "lat":data.get("lat"),
                "lng":data.get("lng")
            }},
            upsert=True
        )
    
    
def saveStationToDatabase(data):
    # Set up client for MongoDB
    
    db=mongoClient.Velov
    c_Station=db.Station
    c_Station.insert_one(data)


def run():
    client = connect_mqtt()
    subscribe(client,"getStation")
    subscribe(client,"getStationName")
    client.loop_forever()


if __name__ == '__main__':
    run()
