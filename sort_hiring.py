import gspread
from oauth2client.service_account import ServiceAccountCredentials
from credentials.read_creds import get_creds

creds = get_creds()
file = gspread.authorize(creds) 
sheet = file.open("S23 Available Students for Hourly Positions")
sheet = sheet.get_worksheet(0)


list_of_lists = sheet.get_all_values()[2:]

list_of_lists = sorted(list_of_lists, key= lambda x : x[1])


sheet.update('A3', list_of_lists)

list_of_lists = sheet.get_all_values()[2:]

for i, row in enumerate(list_of_lists):
    if row[1].strip().lower() == "hired":
        sheet.format(f"A{i+3}:P", {
        "backgroundColor": {
        "red": 1.0
        }})
        break



