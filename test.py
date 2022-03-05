from urllib import response
import requests

url_param = ["add", "sub", "mul", "div", "lcm", "hcf", "quadratic", "linear2var"]


for u in url_param:
    response_data = requests.get(f"http://127.0.0.1:5000/{u}", json={"type": 1, "difficulty": 1, "noq": 1, "params": {"number_of_nums": 4}})
    if not response_data.ok: raise Exception("Response Not OK")
    for r in response_data.json():
        print(r)

