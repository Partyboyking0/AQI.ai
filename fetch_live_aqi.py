import requests
from stations import STATIONS

def get_all_aqi():
    data = {}
    for s in STATIONS:
        res = requests.get(f"http://127.0.0.1:8000/predict/{s}")
        data[s] = round(res.json().get("aqi",0),2)
    return data
