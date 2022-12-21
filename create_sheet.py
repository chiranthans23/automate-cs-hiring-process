
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from credentials.read_creds import get_creds


creds = get_creds()
file = gspread.authorize(creds) 
sh = file.create('Test spreadsheet')
sh.share('**@colorado.edu', perm_type='user', role='writer')
sh.share('**@colorado.edu', perm_type='user', role='writer')