"""
This script sorts people in the available students sheet
Puts hired students at the buttom with red color and rest on the top

"""


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from credentials.read_creds import authenticate
from config.config import cfg 


def sort_sheet_hired():
    file = authenticate()
    sheet = file.open(cfg['students_sheet_name'])
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


if __name__ == '__main__':
    sort_sheet_hired()

