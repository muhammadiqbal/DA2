import json
import requests
import csv

data = {}
data = json.dumps(data)
token = "2fad3ffb3f654b17a3d60ccad6ddc26d"
url4D = "http://optim.uni-muenster.de:5000/api/"+token

headers = {'Content-Type': 'application/json'}
file = csv.writer(open("realData4D.csv", "a+"), delimiter=';')

file.writerow(["x1","x2","x3","x4","data"])
for x in range(0,10):
	for y in range (0,10):
		# url = url4D+"/"+str(x/10)+","+str(y/10)+","+str(x/10)+","+str(y/10)
		response = requests.get(url,headers=headers)
		print(url)
		restResponse = json.loads(response.content.decode('utf-8'))
		file.writerow([str(x/10),str(y/10), str(x/10),(y/10), restResponse["data"]])
print("done!")

