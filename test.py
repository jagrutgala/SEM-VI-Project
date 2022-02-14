from urllib import response
import requests

response_data = requests.get("http://127.0.0.1:5000/", json={"data": "Hello World"})

if response_data.ok:
    print(response_data.json())