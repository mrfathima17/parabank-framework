import json
from pages.login_page import LoginPage
from pages.findtransaction_page import FindTransactionPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_find_transaction_by_amount(page):
    login = LoginPage(page)
    find = FindTransactionPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    find.go_to_find_transactions(page)
    page.wait_for_timeout(2000)
    find.search_by_amount(data["find_transaction"]["amount"])
    page.wait_for_timeout(2000)
    assert find.is_results_table_visible() or \
           "No transactions found" in page.content()

def test_find_transaction_by_date(page):
    login = LoginPage(page)
    find = FindTransactionPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    find.go_to_find_transactions(page)
    page.wait_for_timeout(2000)
    find.search_by_date(data["find_transaction"]["date"])
    page.wait_for_timeout(2000)
    assert find.is_results_table_visible() or \
           "No transactions found" in page.content()