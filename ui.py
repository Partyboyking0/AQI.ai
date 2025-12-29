
import streamlit as st
import requests

st.markdown("""
<style>
body {background-color:#0f1115;}
.card {
    background:#2b2f36;
    padding:25px;
    border-radius:20px;
    color:white;
    box-shadow:0 0 20px rgba(255,0,0,0.2);
}
.big-aqi {font-size:60px;color:#ff3c3c;font-weight:bold;}
.sub {color:#bbb;}
.header {
    background:#1b1f24;
    padding:30px;
    border-radius:35px;
    text-align:center;
}
.map-box {
    background:white;
    border-radius:25px;
    padding:20px;
}
</style>
""", unsafe_allow_html=True)


# st.set_page_config(page_title="Delhi Smart City AQI", layout="centered")

st.markdown("""
<div class="header">
<h1 style="color:white">AQI.ai</h1>
<h3 style="color:#aaa">New Delhi Air Quality Index | Smart City Dashboard</h3>
<p class="sub">Real‑time hyper‑local air quality intelligence</p>
</div>
""", unsafe_allow_html=True)

location = st.selectbox("Select Monitoring Station", 
                         ["Wazirpur","Siri Fort","Anand Vihar"])

col1, col2 = st.columns([1,2])

with col1:
    if st.button("Predict"):
        try:
            res = requests.get(f"http://127.0.0.1:8000/predict/{location}", timeout=5)
            data = res.json()

            if "aqi" in data:
                aqi = round(float(data["aqi"]),2)
                st.markdown(f"""
                            <div class="card">
                            <div class="big-aqi">{aqi}</div>
                            <p class="sub">Predicted AQI for {location}</p>
                            </div>
                            """, unsafe_allow_html=True)

                if aqi <= 50:
                    st.success("🟢 Good – Air is clean and healthy")
                elif aqi <= 100:
                    st.info("🟡 Satisfactory – Minor breathing discomfort")
                elif aqi <= 200:
                    st.warning("🟠 Moderate – Sensitive groups affected")
                elif aqi <= 300:
                    st.error("🔴 Poor – Avoid prolonged outdoor exposure")
                elif aqi <= 400:
                    st.error("🟣 Very Poor – Respiratory illness risk")
                else:
                    st.error("⚫ Severe – Stay indoors, health emergency")

            else:
                st.error(data.get("error","Backend error"))

        except Exception:
            st.error("Backend is not reachable. Please start FastAPI server.")

with col2:
    from aqi_gis_map import create_map
    from fetch_live_aqi import get_all_aqi
    import streamlit.components.v1 as components
    import folium

    if st.button("🌍 Show Delhi AQI Map"):

        aqi_data = get_all_aqi()
        m = create_map(aqi_data)

        html = m._repr_html_()
        components.html(html, height=650)
