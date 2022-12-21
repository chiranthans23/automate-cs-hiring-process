
import gspread
from config.config import cfg 

gc = gspread.oauth(
    credentials_filename='./credentials/oauth_key.json',
    authorized_user_filename='./credentials/authorized_user.json'
)


sheet = gc.open('CSEN CM/Grader Application 2022 and beyond (Responses)')

sheet = sheet.get_worksheet(0)
print(sheet)
