from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "http://api.b365api.com/v3/events/inplay?sport_id=18&token=219761-iALwqep7Hy1aCl"

def fetch_games():
    try:
        res = requests.get(API_URL)
        if res.status_code == 200:
            return res.json().get("results", [])
    except Exception as e:
        print("Error:", e)
    return []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/games')
def games():
    return jsonify(fetch_games())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
