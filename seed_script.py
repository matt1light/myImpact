import requests, json

URL = "http://172.30.182.36:8000/raw_datas/"

#------------------------------------------------------------------------------
#SEED TRASH
#------------------------------------------------------------------------------

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 5.2 kg", "dateTime": "2019-01-20 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 6.32 kg", "dateTime": "2019-01-20 011:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 3.2 kg", "dateTime": "2019-01-21 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 1.32 kg", "dateTime": "2019-01-21 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 4.42 kg", "dateTime": "2019-01-22 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 8.2 kg", "dateTime": "2019-01-22 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 3.2 kg", "dateTime": "2019-01-23 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 5.62 kg", "dateTime": "2019-01-23 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 9.2 kg", "dateTime": "2019-01-24 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 1.22 kg", "dateTime": "2019-01-24 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 1.62 kg", "dateTime": "2019-01-25 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 4.52 kg", "dateTime": "2019-01-25 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 2.12 kg", "dateTime": "2019-01-26 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 3.2 kg", "dateTime": "2019-01-26 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 6.2 kg", "dateTime": "2019-01-27 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "trash", "boardId": "1A2S3D", "data": " /d/d 4.2 kg", "dateTime": "2019-01-27 11:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

#------------------------------------------------------------------------------
#SEED WATER
#------------------------------------------------------------------------------

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  121.3 L", "dateTime": "2019-01-20 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  145.3 L", "dateTime": "2019-01-21 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  132.33 L", "dateTime": "2019-01-22 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  98.23 L", "dateTime": "2019-01-23 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  134.3 L", "dateTime": "2019-01-24 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  123.13 L", "dateTime": "2019-01-25 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  111.3 L", "dateTime": "2019-01-26 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "water", "boardId": "1A2B3C", "data": "  132.3 L", "dateTime": "2019-01-27 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

#------------------------------------------------------------------------------
#SEED ELECTRICITY
#------------------------------------------------------------------------------

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 12.0, "unit": "kWh"}, "dateTime": "2019-01-20 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 121.0, "unit": "kWh"}, "dateTime": "2019-01-21 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 112.1, "unit": "kWh"}, "dateTime": "2019-01-23 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 123.3, "unit": "kWh"}, "dateTime": "2019-01-24 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 90.1, "unit": "kWh"}, "dateTime": "2019-01-25 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 98.01, "unit": "kWh"}, "dateTime": "2019-01-26 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "electricity", "boardId": "1W2E3R", "data": {"value": 102.0, "unit": "kWh"}, "dateTime": "2019-01-27 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)


#------------------------------------------------------------------------------
#SEED GAS
#------------------------------------------------------------------------------

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 121.4, "unit": "MJ"}, "dateTime": "2019-01-20 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 121.4, "unit": "MJ"}, "dateTime": "2019-01-21 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 121.4, "unit": "MJ"}, "dateTime": "2019-01-22 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 131.4, "unit": "MJ"}, "dateTime": "2019-01-23 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 111.34, "unit": "MJ"}, "dateTime": "2019-01-24 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 121.14, "unit": "MJ"}, "dateTime": "2019-01-25 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 111.84, "unit": "MJ"}, "dateTime": "2019-01-26 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)

data = '{"deviceType": "gas", "boardId": "1S3D3A", "data": {"value": 129.14, "unit": "MJ"}, "dateTime": "2019-01-27 09:21:39.293248"}'
print("[POST]: " + data + " to " + URL)
r = requests.post(URL, json.loads(data))
print(r.status_code, r.reason)
