"""
finds the number of available roles for each subject
updates the sheet with red when a course has all the roles filled

"""

from credentials.read_creds import authenticate
from config.config import cfg 


def update_roles():
    file = authenticate()

    sheet = file.open(cfg['available_roles_sheet_name'])
    sheet = sheet.get_worksheet(0)

    list_of_lists = sheet.get_all_values()[1:]

    courses = {}

    for row in list_of_lists:
        if not row[0].strip().startswith("CSCI"):
            continue

        classes = [ ele.split("-")[0].strip() for ele in row[0].strip().split(",")]

        classe = ", ".join(classes)

        courses[classe] = {}
        courses[classe]['CM'] = 0 if row[3].strip()=="" else int(row[3].strip())
        courses[classe]['Grader'] = 0 if row[4].strip()=="" else int(row[4].strip())


    sheet = file.open(cfg['copy_of_offered_students_sheet_name'])
    sheet = sheet.get_worksheet(0)

    list_of_lists = sheet.get_all_values()[1:]


    for row in list_of_lists:
        classe = ", ".join([ ele.split("-")[0].strip() for ele in row[6].strip().split(",")])

        if row[5] == 'CM':
            courses[classe]['CM']-= 1
        elif row[5] == 'Grader':
            courses[classe]['Grader']-= 0 if row[7].strip()=="" else int(row[7].strip())

    # for k, v in courses.items():
    #     if courses[k]['CM'] <= 0 and courses[k]['Grader'] <= 0:
    #         print(f"Course : {k}, Roles: {v}")

    # return 

    sheet = file.open(cfg['available_roles_sheet_name'])
    sheet = sheet.get_worksheet(0)

    list_of_lists = sheet.get_all_values()[1:]

    

    for i, row in enumerate(list_of_lists):
        if not row[0].strip().startswith("CSCI"):
            continue

        classe = ", ".join([ ele.split("-")[0].strip() for ele in row[0].strip().split(",")])

        if classe not in courses: # formatting problem or there is some error
            continue


        if courses[classe]['CM'] <= 0 and courses[classe]['Grader'] <= 0:
            sheet.format(f"A{i+2}:E{i+2}", {
            "backgroundColor": {
            "red": 1.0
            }})

    return 




if __name__ == "__main__":


    update_roles()
