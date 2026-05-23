import json
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_transfer_funds(page):
    login = LoginPage(page)
    transfer = TransferPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    transfer.go_to_transfer(page)
    page.wait_for_timeout(2000)
    transfer.transfer_funds(data["transfer"]["amount"])
    page.wait_for_timeout(2000)
    assert "Transfer Complete" in transfer.get_success_message()

def test_transfer_zero_amount(page):
    login = LoginPage(page)
    transfer = TransferPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    transfer.go_to_transfer(page)
    page.wait_for_timeout(2000)
    transfer.transfer_funds("0")
    page.wait_for_timeout(2000)
    content = page.content()
    assert "Transfer Complete" in content
    assert "$0.00" in content

def test_transfer_page_loads(page):
    login = LoginPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    page.goto("https://parabank.parasoft.com/parabank/transfer.htm")
    page.wait_for_timeout(2000)
    assert "Transfer Funds" in page.content()