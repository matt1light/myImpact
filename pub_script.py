import paho.mqtt.publish as publish
print('Sending {"test": 1} to topic testing')
publish.single("testing", '{"test": 1}', hostname="localhost")
