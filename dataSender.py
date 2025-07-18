import time
import random
import requests

base_lat = 27.7172
base_lon = 85.3240

# server url below
server_url = "http://localhost:5000/gps" # gps is the route to app.py


# locations demo
while True:
    lat = base_lat + random.uniform(-0.003,0.003)
    lon = base_lon + random.uniform(-0.003,0.003)

    data = {
        "busID": "BUS_01",
        "latitude": round(lat,6),
        "longitude": round(lon,6),
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    print(f"[Unreal] Sending: {data}")

    try:
        response = requests.post(server_url,json=data)
        print(f"[Server Response] {response.status_code} - {response.json()}")
    except requests.exceptions.RequestException as e:
        print("[Error] Failed to send data:",e)

    time.sleep(5)