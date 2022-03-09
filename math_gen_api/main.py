# math_gen_api/main.py

# In-built imports
from pydoc_data.topics import topics
from typing import Any, Dict, Optional, Tuple

# Third-party imports
from flask import Flask, jsonify, request, render_template
from flask.wrappers import Response

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from math_gen_api.question_generator import COMBINE_LOOKUP, Question_Generator
from question_strategies import question

##############################
# Flask API Init
##############################
app = Flask(__name__)
app.config["ENV"] = "development"

# global question generator factory

def readRequestData(req_data) -> Tuple[int, int, dict[str, Any]]:
    type_ = req_data.get("type", 1)
    noq = req_data.get("noq", 1)
    params = req_data.get("params", {})
    return (type_, noq, params)

def createErrorResponse(err_message, err_code):
    return Response(err_message, err_code)

##############################
# Documentation Routes
##############################
@app.route("/", methods=["GET"])
def index(): # url navigation info
    return render_template("index.html")

@app.route("/available topics", methods=["GET", "OPTIONS"])
def topicOptions():
    options = COMBINE_LOOKUP.keys()
    if options == None: return createErrorResponse("Invalid Topic", 404)
    return jsonify(list(options))

@app.route("/available types", methods=["GET", "OPTIONS"])
def typeOptions():
    q_topic = request.args.get("topic")
    if q_topic == None: return createErrorResponse("Invalid Argument", 400)
    options = COMBINE_LOOKUP.get(q_topic)
    if options == None: return createErrorResponse("Invalid Topic", 404)
    return jsonify(list(range(1, len(options)+1)))

##############################
# Question Routes
##############################
@app.route("/question")
def questionRoute():
    json_data = request.get_json()
    if json_data == None: return render_template("question_docs.html")
    q_topic:str = json_data.get("q_topic", None)
    q_type:int = json_data.get("q_type", None)
    noq:int = json_data.get("noq", 1)
    ll:Optional[int] = json_data.get("ll", None)
    ul:Optional[int] = json_data.get("ul", None)
    args:Optional[Dict[str, Any]] = json_data.get("args", None)
    if not all((q_topic,q_type)): return createErrorResponse("Error - Bad Request", 400)
    question_list:list = []
    for _ in range(noq):
        question_generator:Optional[question.QuestionType] = Question_Generator(q_topic, q_type, ll, ul, args)
        if question_generator == None: return createErrorResponse("Error - Bad Arguments 1", 400)
        try:
            q:question.Question = question_generator.generate_question()
        except Exception:
            return createErrorResponse("Error - Bad Arguments 2", 400)
        question_list.append(q.toDict())
    return jsonify(question_list)

@app.route("/random")
def randomQuestion():
    return "Random Question Generating"

if __name__ == "__main__":
    app.run(debug=True)
