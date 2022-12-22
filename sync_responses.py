"""
This logic syncs the data from the original response 
sheet from the students (which is write protected)
to the sheet that's accessible the instructors

"""

from credentials.read_creds import authenticate
from config.config import cfg 
from sort_hiring import sort_sheet_hired

def sync_resp():
    file = authenticate()

    res = []

    sheet = file.open(cfg['student_responses_sheet_name'])
    sheet = sheet.get_worksheet(0)
    list_of_lists = sheet.get_all_values()[2:]

    for row in list_of_lists:
        if "Course Manager" in row[5] or "Grader" in row[5] or "Both" in row[5]:
            res.append(["", "Available"] + row[1:])

    n1 = len(res)

    sheet = file.open(cfg['students_sheet_name'])
    sheet = sheet.get_worksheet(0)
    list_of_lists = sheet.get_all_values()[2:]

    n2 = len(list_of_lists)


    n = n1 - n2

    if n <= 0:
        return #something is wrong or it's up-to-date
        

    list_of_lists.extend(res[-n::])

    sheet.update('A3', list_of_lists)

    sort_sheet_hired()


if __name__ == "__main__":
    sync_resp()


