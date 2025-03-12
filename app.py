from flask import Flask
import folium
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return "À propos de moi : Je suis en train d'apprendre à développer des applications web avec Flask !"

def about():
# coordGareFrethun=(50.901235, 1.811054)
# coordGareCalaisVille=(50.9536, 1.8509)
# coordUniversite=(50.9532, 1.8804)


if.request.methode =='POST':
    destination = request.form.get('destination')

m = folium.Map(location=(50.95,1.88), zoom_start=12,tiles="cartodb positron") #lat,long
folium.Marker(
    location=[coordUniversite[0],coordUniversite[1]],
    tooltip="Click me!",
    popup="Université",
    icon=folium.Icon(icon='1', prefix='fa', color='red'),
).add_to(m)

folium.Marker(
    location=[coordGareCalaisVille[0],coordGareCalaisVille[1]],
    tooltip="Click me!",
    popup="Gare Calais ville",
    icon=folium.Icon(icon='2', prefix='fa', color='blue'),
).add_to(m)

folium.Marker(
    location=[coordGareFrethun[0],coordGareFrethun[1]],
    tooltip="Click me!",
    popup="Gare Calais Frethun",
    icon=folium.Icon(icon='3', prefix='fa', color='green'),
).add_to(m)

distance = geodesic(coordUniversite, coordGareFrethun).kilometers
folium.PolyLine(locations=[coordUniversite, coordGareFrethun], color='blue').add_to(m)
folium.Marker(location=[(coordUniversite[0] + coordGareFrethun[0]) / 2, (coordUniversite[1] + coordGareFrethun[1]) / 2],
              icon=folium.DivIcon(html=f'<div style="font-size: 12pt; color: blue;">{distance:.2f} km</div>')).add_to(m)

distance = geodesic(coordUniversite, coordGareCalaisVille).kilometers
folium.PolyLine(locations=[coordUniversite, coordGareCalaisVille], color='blue').add_to(m)
folium.Marker(location=[(coordUniversite[0] + coordGareCalaisVille[0]) / 2, (coordUniversite[1] + coordGareCalaisVille[1]) / 2],
              icon=folium.DivIcon(html=f'<div style="font-size: 12pt; color: blue;">{distance:.2f} km</div>')).add_to(m)


return render_template('about.html')