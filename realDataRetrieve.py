import json
import requests
import csv

data = {}
data = json.dumps(data)
token = "2fad3ffb3f654b17a3d60ccad6ddc26d"
url4D = "http://optim.uni-muenster.de:5000/api-test4D/"+token

headers = {'Content-Type': 'application/json'}
file = csv.writer(open("test4D.csv", "w+"), delimiter=';')

file.writerow(["vx1","vx2","vx3","vx4", "v2x1","v2x2","v2x3","v2x4","data[0]","data[1]"])
for x in range(0,10):
	url = url4D+"/"+str(x/10)+","+str(x/10)+","+str(x/10)+","+str(x/10)+";"+str(x/10)+","+str(x/10)+","+str(x/10)+","+str(x/10)
	response = requests.get(url,headers=headers)
	print(url)
	restResponse = json.loads(response.content.decode('utf-8'))
	file.writerow([str(x/10),str(x/10), str(x/10),(x/10),str(x/10),str(x/10), str(x/10),(x/10), restResponse["data"],restResponse["data"]])
print("done!")

