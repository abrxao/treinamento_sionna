import folium
import pandas as pd

SEARCH_ADDRESS = "AV BEIRA MAR"
SEARCH_PROVIDER = "CLARO"

bases = pd.read_csv("bases_5g_fortaleza.csv")
bases = bases[bases["Empresa Fistel"] == SEARCH_PROVIDER]
bases = bases[bases["EnderecoEstacao"] == SEARCH_ADDRESS]

lat_and_long = []

for index, row in bases.iterrows():
    lat_and_long.append({"name": row["EndComplemento"], "coordinates":[row["Latitude"], row["Longitude"]]})

starting_point = lat_and_long[0]["coordinates"]
points_map = folium.Map(starting_point, zoom_start=50)

for location in lat_and_long:
    folium.Marker(location["coordinates"], popup=location["name"], tooltip=location["name"]).add_to(points_map)
    
points_map.save("map.html")