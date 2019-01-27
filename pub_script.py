import paho.mqtt.publish as publish

data = '{"deviceType": "trash", "boardId": "1A2B3C", "data": " /d/d 12.32 kg"}'
print('Sending ' + data + ' to topic rawData')
publish.single("rawData", data, hostname="localhost")
