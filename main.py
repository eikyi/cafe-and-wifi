import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
BASE_URL = os.environ.get('CAFE_API_BASE_URL')
DELETE_API_KEY = os.environ.get('DELETE_API_KEY')
Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/list")
def get_all_cafe():
    #reqest all cafe data
    response_all_cafe = requests.get(f"{BASE_URL}all")
    response_all_cafe.raise_for_status()
    cafes = response_all_cafe.json()['cafes']

    return render_template('cafe-list.html',cafes = cafes)

@app.route("/details/<cafe_id>")
def cafe_details(cafe_id):
    response_cafe = requests.get(f"{BASE_URL}search?id={cafe_id}")
    response_cafe.raise_for_status()
    cafe = response_cafe.json()['cafes'][0]
    return render_template('cafe-details.html',cafe=cafe)

@app.route("/close/<cafe_id>")
def close_cafe(cafe_id):
    response = requests.delete(f"{BASE_URL}report-closed/{cafe_id}?api-key={DELETE_API_KEY}")
    response.raise_for_status()
    return redirect(url_for('get_all_cafe'))

if __name__ == "__main__":
    app.run(debug=False)