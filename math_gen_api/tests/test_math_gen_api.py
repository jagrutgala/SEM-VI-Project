import requests

question_options ={
    "q_topic": "linear2var",
    "q_type": "normal",
    "noq": 12,
    "ll": 10,
    "ul": 28
}

def question_request(question_options:dict):
    # response_data = requests.get(f"http://127.0.0.1:5000/question", json=question_options)
    response_data = requests.get(f"http://127.0.0.1:5000/question", params=question_options)
    print(response_data.request.url)
    if not response_data.ok:
        print(response_data.text)
    for r in response_data.json():
        print(r)

def topic_request():
    response_data = requests.get(f"http://127.0.0.1:5000/available topics")
    if not response_data.ok:
        print(response_data.text)
    return response_data.json()

def type_request(type_:str):
    response_data = requests.get(f"http://127.0.0.1:5000/available types", params={f"topic":{type_}})
    if not response_data.ok:
        print(response_data.text)
    for r in response_data.json():
        print(r)


if __name__ == "__main__":
    # Code Here
    question_request(question_options)
    # topic_request()
    # type_request("square")