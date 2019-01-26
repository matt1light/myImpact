import paho.mqtt.client as mqtt
import requests, json, datetime

def on_raw_data(mosq, obj, msg):
    print("MESSAGES: " + msg.topic + " " + str(msg.payload))
    post_data(json.loads(msg.payload.decode('utf8')))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def post_data(data):
    data['datetime'] = str(datetime.datetime.now())
    r = requests.post("http://localhost:3000/test", data)
    print(r.status_code, r.reason)

mqttc = mqtt.Client()

mqttc.message_callback_add("raw_data", on_raw_data)
mqttc.on_message = on_message
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("testing", 0)

mqttc.loop_forever()
