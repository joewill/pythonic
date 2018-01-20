def find_accounts(search_text):

    if not db_is_available:
        return None

    # returns a list of account IDs
    return db_search(search_text)


accounts = find_accounts('python')
# if accounts is None, proper way to test for this
if accounts is None:
    print("Error, db is not available")
else:
    print("Accounts found: Would list them here...")
