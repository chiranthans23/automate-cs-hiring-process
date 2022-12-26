"""
sync new responses submitted by students, fetches new hired students
and also sorts the hired ppl

"""

from sync_responses import sync_resp
from sync_hired_ppl import sync_hired
from sort_hiring import sort_sheet_hired

if __name__ == "__main__":
    sync_resp()
    sync_hired()
    sort_sheet_hired()