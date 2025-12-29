from fastapi import FastAPI, requests
import pandas as pd
import numpy as np
import joblib
import os
from tensorflow.keras.models import load_model

app = FastAPI()

# ================= LOAD MODEL & TOOLS =================

BASE = os.path.dirname(os.path.abspath(__file__))

model = load_model(os.path.join(BASE,"delhi_region_aqi_lstm.h5"), compile=False)
scaler = joblib.load(os.path.join(BASE,"aqi_scaler.pkl"))
le = joblib.load(os.path.join(BASE,"location_encoder.pkl"))

# ================= LOAD HISTORY =================

history = pd.read_csv(os.path.join(BASE,"sensor_history.csv"))
history['event_timestamp'] = pd.to_datetime(history['event_timestamp'])
LOCATION_MAP = {
    "wazirpur": "Delhi Institute of Tool Engineering, Wazirpur, Delhi, Delhi, India",
    "siri fort": "Siri Fort, Delhi, Delhi, India",
    "anand vihar": "Anand Vihar, Delhi, Delhi, India"
}

# Keep only trained columns (drop any extra CSV columns)
features = ['temperature','humidity','pressure','wind_speed','wind_direction',
            'pm25','pm10','no2','so2','o3','co']

history = history[['location_id','event_timestamp'] + features]

# ================= PREDICTION API =================

@app.get("/predict/{location}")
def predict_auto(location: str):

    region = history[history['location_id'].str.lower().str.contains(location.lower())] \
                .sort_values("event_timestamp")


    if len(region) < 24:
        return {"error":"Need at least 24 hourly records for this region"}

    region = region.tail(24)

    X = scaler.transform(region[features].values)

    key = location.lower().strip()
    full_name = LOCATION_MAP.get(key)

    if full_name not in le.classes_:
        return {"error":"Station not supported by model"}

    loc = le.transform([full_name])[0]

    L = np.full((1,24), loc)

    pred = model.predict([L, X.reshape(1,24,11)], verbose=0)[0][0]
    return {"aqi": round(float(pred),2)}

@app.get("/stations")
def get_stations():
    return sorted(list(LOCATION_MAP.keys()))


@app.get("/predict_all")
def predict_all():
    data = {}
    for s in LOCATION_MAP.keys():
        data[s.title()] = requests.get(f"http://127.0.0.1:8000/predict/{s}").json().get("aqi",0)
    return data

