import json
import os
import openpyxl

s = open("roles.json", "r")
x = open("RoleInfo.csv", "w")
role_res = s.read()

t = json.loads(role_res)
roleid = []
for i in t['_embedded']['roles']:
        print(i['role_id'])
        roleid.append(i['role_id'])

s.close()


