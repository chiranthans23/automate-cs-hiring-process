"""
    syncs the roles from the master sheet to the copied sheet
    then updates the available roles
"""
from sync_offers import sync_offers
from update_available_roles import update_roles

def main():
    sync_offers()
    update_roles()


if __name__ == "__main__":
    main()

