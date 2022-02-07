# API
from urllib import response
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.config["ENV"] = "development"

@app.route("/", methods=["GET", "OPTIONS"])
def index():
    return render_template("index.html")

@app.route("/basic")
def basicRoute():
    data = request.get_json()
    if data is None: return "Error 400"
    difficulty = data.get("difficulty", None)
    operator = data.get("operator", None)
    


# @app.route("/path", methods=["GET", "POST", "PUT", "DELETE"])
# def template_route():
#     pass

if __name__ == "__main__":
    app.run(debug=True)
