from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = "YOUR_BETSAPI_KEY"
API_URL = "https://api.b365api.com/v3/events/inplay?sport_id=18&token=" + API_KEY

def fetch_live_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json().get("results", [])
    except Exception as e:
        print("Error fetching data:", e)
    return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    games = fetch_live_data()
    return jsonify(games)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
