"""
This keeps the sheet containing the offers given by the instructors
in sync with the copy of it

This is to make any modifications to the copied sheet

"""
from credentials.read_creds import authenticate
from config.config import cfg 

def sync_offers():
    file = authenticate()

    sheet = file.open(cfg['offered_students_sheet_name'])
    sheet = sheet.get_worksheet(0)
    # can change it to 2 when 2 dummy values in the sheet are removed
    list_of_lists1 = sheet.get_all_values()[4:]



    n1 = len(list_of_lists1)

    sheet = file.open(cfg['copy_of_offered_students_sheet_name'])
    sheet = sheet.get_worksheet(0)
    list_of_lists = sheet.get_all_values()[1:]

    n2 = len(list_of_lists)


    n = n1 - n2

    if n <= 0:
        return #something is wrong or it's up-to-date
        

    list_of_lists.extend(list_of_lists1[-n::])

    sheet.update('A2', list_of_lists)



if __name__ == "__main__":
    sync_offers()


