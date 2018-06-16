import json
import requests
import csv

data = {}
data = json.dumps(data)
token = "2fad3ffb3f654b17a3d60ccad6ddc26d"
url4D = "http://optim.uni-muenster.de:5000/api-test4D/"+token+"/0.4,0.1,0.06,0.2;0.2,0.3,0.6,0.2"
url2D = "http://optim.uni-muenster.de:5000/api-test2D/"+token
headers = {'Content-Type': 'application/json'}
file = csv.writer(open("data.csv", "w+"), delimiter=';')

for x in range(0,10):
    for y in range(0,10):
        for x2 in range(0,10):
            for y2 in range(0,10):
                url = url2D+"/"+str(x/10)+","+str(y/10)+";"+str(x2/10)+","+str(y2/10)
                #print(url)
                response = requests.get(url,headers=headers)
                restResponse = json.loads(response.content.decode('utf-8'))
                #print(restResponse)
                #data.append(restResponse)
                file.writerow([str(x/10),str(y/10), str(x2/10),(y2/10), restResponse["data"]])
print("done!")
