from flask import Flask

app = Flask(__name__)

@app_route("/")
def mars_foto():
    return "<p>Hello World!<p>"

app.run(debug=True)
