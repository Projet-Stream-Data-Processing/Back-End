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
        
        print(f"Received message on `{msg.topic}` topic")
        
        
        if msg.topic == "getStation":
            saveStationToDatabase(message)

        elif msg.topic == "getStationName":
            saveNameToDatabase(message);

    client.subscribe(topic)
    client.on_message = on_message
    

def saveNameToDatabase(data):
    # Set up client for MongoDB
    
    db=mongoClient.Velov
    c_StationName=db.StationName
    
    c_StationName.find_one_and_update(
        {"name":data.get("name")},
        {"$set":{"data":data}},
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
