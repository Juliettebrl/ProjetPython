from flask import Flask
import folium
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about', ['GET', 'POST'])
def about():
 
    return render_template('about.html')