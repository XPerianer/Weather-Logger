import subprocess
import json
import time
import requests
from config import *

j = json.loads(subprocess.check_output('dht-sensor 0 DHT22 json',shell=True))
time.sleep(10)
jj = json.loads(subprocess.check_output('dht-sensor 0 DHT22 json',shell=True))
h1 = j['humidity']
h2 = jj['humidity']
t1 = j['temperature']
t2 = jj['temperature']
if(abs(h1 - h2) > 5 or abs(t1 - t2) > 5 or t1 < -200 or t2 < -200 or h1 < -200 or h2 < -200):
 print("Problem")
else:
 str = json.dumps(jj)
 print(str)
 r = requests.post('http://things.ubidots.com/api/v1.6/devices/omega2/?token=' + apitoken, data=jj)
print(r)
