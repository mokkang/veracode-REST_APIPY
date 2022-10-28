import json
import os
import openpyxl

s = open("users.json", "r")  
x = open("AccountInfo.csv", "w")
user_res = s.read()

t = json.loads(user_res) 
uid = []
for i in t['_embedded']['users']:
        print(i['user_id'])   
        uid.append(i['user_id'])

s.close()
