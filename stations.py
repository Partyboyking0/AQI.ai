import pandas as pd
from location_map import LOCATION_MAP

coords = pd.read_csv("station_coords.csv")

STATIONS = {
    row['short_name'].title(): (row['lat'],row['lon'])
    for _,row in coords.iterrows()
}
