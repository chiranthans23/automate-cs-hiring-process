"""
    Given a course or list of courses, script creates new sheet
    with students who've applied for the given course(s)
    and provides access to the instructor

"""

import gspread
from credentials.read_creds import authenticate
from config.config import cfg 


def filter_course(courses, instructor):
    res = []

    file = authenticate()
    sheet = file.open(cfg['students_sheet_name'])
    sheet = sheet.get_worksheet(0)


    list_of_lists = sheet.get_all_values()[2:]


    res.append(["Email Address","First Name, Last Name", "Which position are you applying for?", "Your  major",	"If you are not a CS Major, please let us know the name of the faculty member who invited you to apply. Write N/A if it is not applicable.", "Your degree",	"Have you completed the selected course/s at CU Boulder during your academic career?",	"If yes, which courses have you completed.",	"Have you had any other experience related to the selected course/s. Please explain. Please DO NOT add details from your resume on this response.",	"Share your resume link."])
    
    for row in list_of_lists:
        for course in courses:
            if (course in row[10] or course in row[11]) and row[1] == 'Available':
                res.append(row[2:4]+row[6:10]+row[12:])
                break

    sh = file.create('_'.join(courses))
    sh.share('chsr7576@colorado.edu', perm_type='user', role='writer')
    sh.share(instructor, perm_type='user', role='writer')

    sh = sh.add_worksheet(title="Students", rows=1000, cols=10)
    sh.update('A1', res)
    
    sh.format(f"A1:J1", {
            "backgroundColor": {
            "red": 0.678,
            "blue": 0.902,
            "green": 0.847
            }})


if __name__ == '__main__':

    filter_course(["CSCI 5454"], "srirams@colorado.edu")
        

