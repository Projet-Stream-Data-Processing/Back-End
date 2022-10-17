from paho.mqtt import client as mqtt_client
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import random
from Station import Station


broker = '127.0.0.1'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = "admin"
password = "password"

url = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json?maxfeatures=100&start=1"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def getData(url):
    response = requests.get(url)
    return response.json()

def publish(client, message):
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


if __name__ == '__main__':

    server = connect_mqtt()
    server.loop_start()
    #sched = BackgroundScheduler()
    #sched.start()

    # station_list = []
    # data = getData(url)

    # for el in data["values"]:
    #     station = Station(el)
    #     station_list.append(station)
    #     print(station.name)

    publish(server, str("test"))
