import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


def get_creds():
    return ServiceAccountCredentials.from_json_keyfile_name("./credentials/key.json", scopes)

def authenticate():
    gc = gspread.oauth(
    credentials_filename='./credentials/oauth_key.json',
    authorized_user_filename='./credentials/authorized_user.json'
    )
    return gc
