"""
This script syncs people who are hired (from the hired people sheet) 
to the available students sheet

"""


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from credentials.read_creds import authenticate
from config.config import cfg 
from sort_hiring import sort_sheet_hired


def sync_hired():
    file = authenticate()


    sheet = file.open(cfg['hired_students_sheet_name'])
    sheet = sheet.get_worksheet(0)
    list_of_lists = sheet.get_all_values()[2:]

    emails = []

    for row in list_of_lists:
        emails.append(row[4].strip().lower())

    sheet = file.open(cfg['students_sheet_name'])
    sheet = sheet.get_worksheet(0)
    list_of_lists = sheet.get_all_values()[2:]

    for i, row in enumerate(list_of_lists):
        if row[1].lower()!='hired' and row[2].strip().lower() in emails:
            sheet.update_cell(i+3,2, 'Hired')

    sort_sheet_hired()


if __name__ == '__main__':
    sync_hired()




