import requests

question_options ={
    "q_topic": "hcf",
    "q_type": 1,
    "noq": 10,
    "args": {"number_of_nums": 2},
    "ul": 20
}

# for u in url_param:
response_data = requests.get(f"http://127.0.0.1:5000/question", json=question_options)
if not response_data.ok:
    print(response_data.text)
for r in response_data.json():
    print(r)
