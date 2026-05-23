import json
from pages.login_page import LoginPage
from pages.billpay_page import BillPayPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_pay_bill(page):
    login = LoginPage(page)
    billpay = BillPayPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    billpay.go_to_billpay(page)
    page.wait_for_timeout(2000)
    billpay.pay_bill(data["bill_payment"])
    page.wait_for_timeout(2000)
    assert "Bill Payment Complete" in billpay.get_success_message()