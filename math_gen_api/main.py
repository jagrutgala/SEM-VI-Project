# math_gen_api/main.py

# In-built imports
from typing import Any, Dict, Optional, Tuple

# Third-party imports
from flask import Flask, jsonify, request, render_template
from flask.wrappers import Response, Request

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
def createErrorResponse(err_message, err_code):
    return Response(err_message, err_code)

##############################
# Documentation Routes
##############################
@app.route("/")
def index(): # url navigation info
    return render_template("index.html")

@app.route("/docs")
def docs(): # url navigation info
    return render_template("question_docs.html")

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
    return jsonify(list(options.keys()))

##############################
# Question Routes
##############################
@app.route("/question")
def questionRoute():
    request_data = request.get_json()
    # if request_data == None: return createErrorResponse("Bad Request", 400)
    if request_data == None: request_data = request.args.to_dict()
    if request_data is None : return render_template("question_docs.html")
    print("request_data", request_data)
    q_topic:Optional[str] = request_data.get("q_topic", None)
    q_type:Optional[str] = request_data.get("q_type", None)
    noq:int = int(request_data.get("noq", 1))
    ll:Optional[int] = request_data.get("ll", None)
    if ll != None: ll= int(ll)
    ul:Optional[int] = request_data.get("ul", None)
    if ul != None: ul= int(ul)
    if not all((q_topic,q_type)): return createErrorResponse("Error - Bad Request", 400)
    if ll> ul: return createErrorResponse("Error - Bad Limit", 400)
    question_list:list = []
    for _ in range(noq):
        question_generator:Optional[question.QuestionType] = Question_Generator(q_topic, q_type, ll, ul)
        if question_generator == None: return createErrorResponse("Error - Bad Arguments 1", 400)
        try:
            q:question.Question = question_generator.generate_question()
        except Exception as err:
            print(err.args)
            return createErrorResponse("Error - Bad Result 2", 400)
        question_list.append(q.toDict())
    return jsonify(question_list)

if __name__ == "__main__":
    app.run(debug=False)
