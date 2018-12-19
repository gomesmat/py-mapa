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

map = folium.Map(location=[-10,20], zoom_start=2, tiles="Mapbox Bright") #40.629902, -120.831001


fgv=folium.FeatureGroup(name="Vulcões")

for lt, ln, nm, el in zip(lat, lon, nome, el):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=nm, fill_color=colorir(el), color='grey', fill_opacity=0.7))

fgp=folium.FeatureGroup(name="População")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'yellow' if 1000000 <= x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000
else 'orangered' if 100000000 < x['properties']['POP2005'] <= 1000000000
else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map3.html")
