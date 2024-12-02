import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
BASE_URL = os.environ.get('CAFE_API_BASE_URL')
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

@app.route("/details")
def cafe_details():
    return render_template('cafe-details.html')

if __name__ == "__main__":
    app.run(debug=False)