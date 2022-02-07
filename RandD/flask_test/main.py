from urllib import response
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["ENV"] = "development"

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/hello_world")
def hello_world():
    return request.get_json()

@app.route("/<string:q_type>/<int:no_of_questions>", methods=['GET', 'POST', "PUT", "DELETE"])
def mathQuestionGen(q_type, no_of_questions):
    response_data = {}
    if request.method == "GET":
        response_data["method"] = "GET"
    elif request.method == "POST":
        response_data["method"] = "POST"

    return jsonify({"type": q_type, "no": no_of_questions})

if __name__ == "__main__":
    app.run(debug=True)