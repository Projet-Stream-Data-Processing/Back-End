import datetime
from sqlite3 import Timestamp
from apscheduler.schedulers.background import BackgroundScheduler
from API.getData import getStations
from mqtt import connect_mqtt
import json



def publish(client, message, topic="default"):
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    return 1

def sendData(client,init=False):
    """
    Send data to mqtt client

    """
    timestamp = str(datetime.datetime.now())
    topic = "getStation"
    if init:
        topic = "getStationName"
    stations = getStations()
    for station in stations:
        publish(client,json.dumps(station.json(init)),topic=topic)


if __name__ == '__main__':
    client = connect_mqtt()
    client.loop_start()
    
    sched = BackgroundScheduler()
    sched.start()

    # add scheduler for getStation
    # bikes infos
    sched.add_job(sendData, 'interval', args=[client], seconds=60, misfire_grace_time=30)
    # add scheduler for getStationName
    # all infos
    sched.add_job(sendData, 'interval', args=[client,True], hours=1, misfire_grace_time=30)
    
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        exit("ask by user")
    
    
