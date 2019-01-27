import paho.mqtt.client as mqtt
import requests, json, datetime, os
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST")
URL = os.getenv("URL")

print(URL)

def on_message_msgs(mosq, obj, msg):
    print("MESSAGES: " + msg.topic + " " + str(msg.payload))
    post_data(json.loads(msg.payload.decode('utf8')))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def post_data(data):
    data['dateTime'] = str(datetime.datetime.now())
    r = requests.post(URL, data)
    print(r.status_code, r.reason)

mqttc = mqtt.Client()

mqttc.message_callback_add("rawData", on_message_msgs)
mqttc.on_message = on_message
mqttc.connect(MQTT_HOST, 1883, 60)
mqttc.subscribe("rawData", 0)

mqttc.loop_forever()
