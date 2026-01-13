🌆 Delhi Smart City AQI Prediction & GIS Visualization System

A full-stack AI + GIS powered Smart City dashboard that predicts next-hour Air Quality Index (AQI) for major CPCB monitoring stations in Delhi and visualizes them on an interactive Delhi district map using GeoPandas.

This system combines deep learning (LSTM), geospatial analytics, and modern web UI to provide real-time air quality intelligence for citizens and authorities.

🚀 What This Project Does

• Predicts next-hour AQI for every major Delhi CPCB monitoring station
• Uses a deep learning LSTM time-series model trained on 24 years of pollution data
• Visualizes predicted AQI values on an interactive Delhi GIS map
• Color-codes air quality severity (Good → Severe)
• Provides a Smart City style web dashboard for public awareness and decision making

📊 Dataset Information

Dataset Source:
https://huggingface.co/datasets/abhinavsarkar/delhi_air_quality_feature_store_processed.csv

Time Span: 2000 – 2024
Total Records: ~2.9 Million rows
Geographical Coverage: CPCB monitoring stations across India (Delhi used for this project)

Dataset Columns
Column	           Description
location_id	       Monitoring station name
event_timestamp    Date & time of reading
temperature	       Ambient temperature
humidity	         Relative humidity
pressure	         Atmospheric pressure
wind_speed	       Wind speed
wind_direction	   Wind direction
pm25	             PM2.5 concentration
pm10	             PM10 concentration
no2	               Nitrogen dioxide
so2	               Sulphur dioxide
o3	               Ozone
co	               Carbon monoxide
aqi	               Calculated Air Quality Index (target) 

🧠 Model Training Strategy
Time-Based Train–Test Split
Period	      Usage
2000 – 2015	  Training Data
2016 – 2024	  Testing Data

Model Used

• LSTM (Long Short-Term Memory) neural network
• 24-hour sliding window input
• Multi-sensor feature learning
• Location-aware embedding

Performance
Metric	                     Score
Mean Absolute Error (MAE)	≈ 16 AQI units

🗺️ GIS & GeoPandas Integration

• India district shapefile was processed using GeoPandas
• Delhi boundary was extracted into a clean GIS layer
• Predicted AQI values are mapped to station coordinates
• Interactive Folium maps render color-coded AQI markers over Delhi

AQI Range	     Category
0–50	         Good
51–100	       Moderate
101–200	       Poor
201–300	       Very Poor
301+	         Severe

🖥️ Web Dashboard

• Streamlit frontend
• GIS map embedded directly inside the dashboard

🌟 Why This Project Stands Out

✔ Deep learning + GIS integration
✔ Real Smart City use-case
✔ Real-time prediction pipeline
✔ Government-grade visualization
✔ Research-ready methodology


🐍 Conda Environment Setup
1️⃣ Create Environment

conda create -n aqi python=3.10
conda activate aqi

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣Run app
uvicorn app:app --reload 

Now in different terminal:
4️⃣ Run ui
streamlit run ui.py


👨‍💻 Author

Parth Chakerwarti
Delhi Smart City AQI Prediction System
2026
