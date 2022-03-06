# math_gen_api/main.py

# In-built imports
from typing import Any, Optional, Tuple

# Third-party imports
from flask import Flask, jsonify, request, render_template

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

##############################
# Flask API Init
##############################
app = Flask(__name__)
app.config["ENV"] = "development"

# global question generator factory

def readRequestData(req_data) -> Tuple[int, int, int, dict[str, Any]]:
    type_ = req_data.get("type", 1)
    noq = req_data.get("noq", 1)
    difficulty = req_data.get("difficulty", 1)
    params = req_data.get("params", {})
    return (type_, noq, difficulty, params)

def checkParams(params, against):
    ...

def makeQuestion():
    ...

def createErrorResponse(err_message):
    ...

##############################
# Documentation Routes
##############################
@app.route("/", methods=["GET"])
def index(): # url navigation info
    is_get = False
    data = None
    if request.method == "GET":
        is_get = True
    data = request.get_json()
    return render_template("index.html", get=is_get, json=data)

# @app.route("/type/<int:topic_id>")
# def typesAvaiable():
#     pass

# @app.route("/param/<string:topic_id>/<int:type_id>")
# def paramsAvaiable():
#     pass

##############################
# Question Routes
##############################
@app.route("/add")
def additionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import addition, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = addition.TYPE_LOOKUP.get(type_, None)
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25), params.get("number_of_nums", 2))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/sub")
def subtractionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import subtraction, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = subtraction.TYPE_LOOKUP.get(type_, None)
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25), params.get("number_of_nums", 2))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/mul")
def multiplicationQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import multiplication, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = multiplication.TYPE_LOOKUP.get(type_, None)
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25), params.get("number_of_nums", 2))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/div")
def divisionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import division, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = division.TYPE_LOOKUP.get(type_, None)
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25), params.get("number_of_nums", 2))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/lcm")
def lcmQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import lcm_hcf, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = lcm_hcf.LCMQuestionType1
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25), params.get("number_of_nums", 2))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/hcf")
def hcfQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import lcm_hcf, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = lcm_hcf.HCFQuestionType1
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25), params.get("number_of_nums", 2))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())

    return jsonify(question_list)

@app.route("/quadratic")
def quadraticQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import quadratic, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = quadratic.TYPE_LOOKUP.get(type_, None)
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/linear2var")
def liinear2varQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    type_, noq, difficulty, params = readRequestData(data)

    from question_strategies import linear2var, question
    from number_gen.integer_number import RangedIntegerNumberGenerator

    question_list = []
    question_generator_cls = linear2var.TYPE_LOOKUP.get(type_, None)
    if question_generator_cls == None: return "Error - Bad Question Type"
    question_generator = question_generator_cls(RangedIntegerNumberGenerator(1, 25))
    
    for i  in range(noq):
        q:question.Question = question_generator.generate_question()
        question_list.append(q.toDict())
    
    return jsonify(question_list)

@app.route("/random")
def randomQuestion():
    return "Random Question Generating"



# @app.route("/path", methods=["GET"])
# def template_route():
#     pass

if __name__ == "__main__":
    app.run(debug=True)
