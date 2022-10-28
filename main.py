import csv
import jpype
import openpyxl
from openpyxl import Workbook, load_workbook 
import json
import os
import math

wb = load_workbook('VAccounts.xlsx')

user_id = "uuid"
role_id = "r_id"
user_name = "uid"
email_address = "email"
role_guid = "ruid"
user_type = "utype"
login_status = "log_status"
team_guid = "t_guid"
teamId = "tid"
login_enabled = "log_enable"
saml_user = "saml"
user_legacy_id = "ulegid"


s = open("users.json", "r")  
x = open("AccountInfo.csv", "w")
user_res = s.read()

t = json.loads(user_res) 
uid = []
for i in t['_embedded']['users']:
        uid.append(i['user_id'])


print(uid)






s.close()






















######################3
with open("name.csv", "w", new_line='') as file:
        wr = csv.writer(file, delimiter=",")
        wr.writeRow('Account', 'Login Name', 'User Name', 'Email Address', 'Custom ID', 'Title', 'Login Enabled', 'Created', 'Is Active', 'Is SAML User', 'Is Platform User', 'Has Elearning Role', 'Is Track Assigned', 'Lifetime Courses Accessed', 'Elearning Manager', 'Elearning Manager Email', 'Track', 'Last Login', 'Custom 1', 'Custom 2', 'Custom 3', 'Custom 4', 'Custom 5', 'Roles', 'Curriculum', 'Teams')


#wr.close()
