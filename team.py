import json
import os
import openpyxl

s = open("teams.json", "r")
x = open("TeamInfo.csv", "w")
team_res = s.read()

z = json.loads(team_res)
y = json.loads(team_res)
p = json.loads(team_res)

tuid = []
team_name = []
buid = []
#oid = []
for i in z['_embedded']['teams']:
	print(i['team_id'])
#	tuid.append(i['team_id'])
for j in y['_embedded']['teams']:
	print(j['team_name'])
	team_name.append(j['team_name'])
for k in p['_embedded']['teams']:
	print(k['business_unit'])
	buid.append(k['business_unit'])
s.close()
