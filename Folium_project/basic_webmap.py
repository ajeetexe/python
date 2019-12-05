import folium
from pandas import read_csv

map1 = folium.Map(location=[25.1516, 84.9818], zoom_start=6, tiles='Mapbox Bright')
fgv = folium.FeatureGroup(name='Volcano')
fgp = folium.FeatureGroup(name='Population')
data = read_csv('document/Volcanoes.txt')
lat = list(data['LAT'])
lan = list(data['LON'])
elev = list(data['ELEV'])


def color_producer(elevation):
    if elevation == 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, el in zip(lat, lan, elev):
    fgv.add_child(folium.Marker([lt, ln], str(el), None, folium.Icon(color=color_producer(lt))))
fgp.add_child(folium.GeoJson((open('document/world.json', 'r', encoding='utf-8-sig').read()), lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties'][
        'POP2005'] < 20000000 else 'red'}))
map1.add_child(
    folium.CircleMarker((25.1516, 84.9818), 6, 'Jehanabad', None, fill_color='blue', color='gray', fill_opacity=0.7))
map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save('html/map1.html')
