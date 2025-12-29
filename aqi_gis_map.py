import geopandas as gpd
import folium
from stations import STATIONS

def create_map(aqi_dict):

    india = gpd.read_file("District_Wise_Shapefile\district.shp")
    delhi = india[india["STATE"] == "DELHI"]
    # Convert GeoDataFrame to JSON dict (important)
    delhi_geojson = delhi.to_json()

    m = folium.Map(location=[28.61,77.23], zoom_start=11)

    folium.GeoJson(delhi_geojson, name="Delhi").add_to(m)

    for s,(lat,lon) in STATIONS.items():
        aqi = aqi_dict.get(s,0)

        if aqi <= 50:
            color = "green"
        elif aqi <= 150:
            color = "orange"
        else:
            color = "red"

        folium.CircleMarker(
            [lat,lon],
            radius=7,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"{s}<br>AQI: {aqi}"
        ).add_to(m)

    return m
