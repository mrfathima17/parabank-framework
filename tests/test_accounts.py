import json
from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_view_accounts(page):
    login = LoginPage(page)
    accounts = AccountsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    assert accounts.is_account_table_visible()

def test_click_account_details(page):
    login = LoginPage(page)
    accounts = AccountsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    accounts.click_first_account()
    page.wait_for_timeout(2000)
    assert "Account Details" in accounts.get_account_detail_heading()