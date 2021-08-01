import json
import time

import requests

data = {}

url = 'http://178.154.226.216/api/ingredients/'
headers = {
    'Content-Type': 'application/json'
}

start_time = time.time()

with open('ingredients.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for data4post in data:
        jdata = {'name': data4post['name'], 'measurement_unit': data4post['measurement_unit']}
        jdata = json.dumps(jdata)
        # print(jdata)
        response = requests.post(url, headers=headers, data=jdata)
        print(response.json())

end_time = time.time()

total_time = end_time - start_time
print(total_time)
