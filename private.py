import random

broker = '127.0.0.1'
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = "admin"
password = "password"
