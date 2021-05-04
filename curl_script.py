import requests
import time

BASE = "http://20.191.46.182:5000/"

while True:
    response = requests.get(BASE + "helloworld")
    print(response.json())
    time.sleep(3)

