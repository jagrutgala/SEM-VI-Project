# API
import random
from typing import Optional, Tuple
from urllib import response
from flask import Flask, jsonify, request, render_template
from lookup import QUESTION_LOOKUP
from lookup import DIFFICULTY_LOOKUP
from question import Question

app = Flask(__name__)
app.config["ENV"] = "development"

# global question generator factory

def readRequestData(req_data) -> Tuple[int, int, int, Optional[dict]]:
    type_ = req_data.get("type", 1)
    noq = req_data.get("noq", 1)
    difficulty = req_data.get("difficulty", 1)
    params = req_data.get("params", None)
    return (type_, noq, difficulty, params)

def checkParams(params, against):
    ...

def makeQuestion():
    ...

def createErrorResponse(err_message):
    ...


### Documentation Routes ###
@app.route("/", methods=["GET"])
def index(): # url navigation info
    is_get = False
    data = None
    if request.method == "GET":
        is_get = True
    data = request.get_json()
    return render_template("index.html", get=is_get, json=data)

@app.route("/type/<int:topic_id>")
def typesAvaiable():
    pass

@app.route("/param/<string:topic_id>/<int:type_id>")
def paramsAvaiable():
    pass

### Functional Routes ###
@app.route("/add")
def additionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    topic:str = "add"
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("add", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls(params.get("number_of_nums", 2))
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/sub")
def subtractionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("sub", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls(params.get("number_of_nums", 2))
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/mul")
def multiplicationQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("mul", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls(params.get("number_of_nums", 2))
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/div")
def divisionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("div", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls(params.get("number_of_nums", 2))
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/lcm")
def lcmQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("lcm", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls(params.get("number_of_nums", 2))
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/hcf")
def hcfQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("hcf", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls(params.get("number_of_nums", 2))
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/quadratic")
def quadraticQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("quadratic", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls()
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/linear2var")
def liinear2varQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)
    question_list = []
    for i  in range(noq):
        question_generator_cls = QUESTION_LOOKUP.get(("linear2var", type_), None)
        if question_generator_cls == None: return "Error - Bad parameters"
        question_generator = question_generator_cls()
        question:Question = question_generator.generate_question(DIFFICULTY_LOOKUP.get(difficulty))
        question_list.append(question.toJson())
    return jsonify(question_list)

@app.route("/random")
def randomQuestion():
    return "Random Question Generating"



# @app.route("/path", methods=["GET"])
# def template_route():
#     pass

if __name__ == "__main__":
    app.run(debug=True)
