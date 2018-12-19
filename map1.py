import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
nome = list(data["NAME"])
el = list(data["ELEV"])

def colorir(eleva):
    if (eleva<2000):
        return 'green'
    elif 2000 <= eleva < 3000:
        return 'yellow'
    elif (eleva >= 3000 and eleva < 4000):
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[40.629902, -120.831001], tiles="Mapbox Bright")


fg=folium.FeatureGroup(name="My Map")

for lt, ln, nm, el in zip(lat, lon, nome, el):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=nm, fill_color=colorir(el), color='grey', fill_opacity=0.7))
map.add_child(fg)

map.save("Map1.html")
