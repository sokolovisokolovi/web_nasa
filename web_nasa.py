from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    get_up = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key=DEMO_KEY")
    json_data = json.loads(get_up.text)
    photo = json_data["latest_photos"]
    return render_template("index.html", photo=photo)

app.run(debug=True)