import json
import os
import openpyxl

s = open("users.json", "r")  
x = open("AccountInfo.csv", "w")
user_res = s.read()

t = json.loads(user_res) 
y = json.loads(user_res)
uid = []
username = []

for i in t['_embedded']['users']:
        print(i['user_id'])   
        uid.append(i['user_id'])
	
for j in y['_embedded']['users']:
	print(j['user_name'])
	username.append(j['user_name'])
#	username.append(j['user_name'])
#i =+ i  
m = [i,j]
s.close()
