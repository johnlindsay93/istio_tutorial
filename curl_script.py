import requests
import time

BASE = "http://20.67.180.192:5000/"

while True:
    response = requests.get(BASE + "services1")
    print(response.json())
    time.sleep(3)

