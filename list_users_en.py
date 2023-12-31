## Listing Firebase users and generating an Excel file with these users. ##

import firebase_admin
from firebase_admin import credentials, auth
from openpyxl import Workbook

# Initializing the Admin SDK
cred = credentials.Certificate('YOUR-CREDENCIAL-KEY.json')
firebase_admin.initialize_app(cred)

# Creating a new workbook and selecting the active sheet
wb = Workbook()
ws = wb.active
ws.title = "Users"

# Writing the header
ws.append(['User_UID', 'Email'])

# Listing the users and adding to Excel
for user in auth.list_users().iterate_all():
    ws.append([user.uid, user.email])

# Saving the file
wb.save("users.xlsx")

print("File saved successfully!")
