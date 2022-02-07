from urllib import request
import requests

mydata = requests.get("http://127.0.0.1:5000/",json={"data": "Hello World"})
print(mydata.text)
# requested_data = requests.get("http://127.0.0.1:5000/", data={"type": "Jagrut"})