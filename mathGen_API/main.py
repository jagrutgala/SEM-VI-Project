# API
from urllib import response
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.config["ENV"] = "development"

# global question generator factory


def checkData(data, keys=None):
    keys = keys if keys is not None else ["topic", "type", "params", "noq"]
    check = all([data.has_key(k) for k in keys])
    return check


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

@app.route("/param/<str:topic_id>/<int:type_id>")
def paramsAvaiable():
    pass

### Functional Routes ###
@app.route("/add")
def additionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "add"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getQuestionType(topic, type_)(**params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/sub")
def subtractionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "sub"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getQuestionType(topic, type_)(**params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/mul")
def multiplicationQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "mul"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getQuestionType(topic, type_)(**params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/div")
def divisionQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "div"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getQuestionType(topic, type_)(**params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/basic")
def basicQuestions():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "basic"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getQuestionType(topic, type_)(**params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/lcm")
def lcmQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "lcm"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/hcf")
def hcfQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "hcf"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/percentage")
def percentageQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "percentage"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/quadratic")
def quadraticQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "quadratic"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/liinear2var")
def liinear2varQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "liinear2var"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/si")
def siQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "si"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/ci")
def ciQuestion():
    data = request.get_json()
    if data is None: return "Error - Bad Request"
    if not checkData(data): return "Error - Bad Request"
    topic = "ci"
    type_ = data.get("type", None)
    if type_ is None: return "Error - Undefined Type of Question"
    params = data.get("params", {"difficulty": 1})
    noq = data.get("noq", 1)
    question_list = []
    for i  in range(noq):
        question = qg.getFunc(topic, type_)(params)
        question_list.append(question.json())
    return jsonify(question_list)

@app.route("/random")
def randomQuestion():
    return "Random Question Generating"



# @app.route("/path", methods=["GET"])
# def template_route():
#     pass

if __name__ == "__main__":
    app.run(debug=True)
