
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from credentials.read_creds import authenticate


file = authenticate()
sh = file.create('Test spreadsheet')
sh.share('chsr7576@colorado.edu', perm_type='user', role='writer')
