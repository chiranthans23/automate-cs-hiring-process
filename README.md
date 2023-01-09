# Scripts to manage CM/CG hiring process

## Getting started

1. Get Access to the list of sheets, similar to the one mentioned in `config.py`
2. Create Oauth2 keys in the GCP using your service account and add them creds folder with names `oauth_key.json` and `authorized_user.json`
3. Install `gspread` and `oauth2client` libraries
4. Set to run any script


## List of scripts and their purpose

1. `connect_oauth.py`: Tester script to check if you have access to a given sheet
2. `create_sheet.py`: Tester script to test creation of sheet and given access to other users
3. `filter_course_students.py`: Filters students who've applied for given list of courses and are available (not hired). It creates a sheet using this data and also provides access to the respective instructor and the script controller
4. `sort_hiring.py`: Sorts students by putting available students to the top of the sheet and others to the bottom and also marking them with red
5. `sync_and_update_roles.py`: Syncs data of people who are fired for a subject and role and based on that updates if all the roles of a subject are hired
6. `sync_hired_ppl.py`: Finds students who are hired and updates availability of those students in the availability sheet
7. `sync_offers.py`: Syncs offeres made to the copy of the sheet. This is to make any modifications needed
8. `sync_resp_hired_sort.py`: This does multiple tasks. Find new responses submitted by students and syncs it to the availability sheet, and also finds newly hired people and mark their availability as hired in the availability sheeet using a red marker
9. `sync_responses.py`: syncs new respones submitted by students
10. `update_available_roles.py`: finds if a subject has all the roles filled and updates it with a red mark if it's filled




