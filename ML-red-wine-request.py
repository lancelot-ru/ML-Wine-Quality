# Посылаем вектор характеристик приложению, получаем ответ (для этого вектора - This wine is good)

import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = [[7.5,0.52,0.16,1.9,0.085,12,35,0.9968,3.38,0.62,9.5]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
