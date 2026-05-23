import json
from pages.login_page import LoginPage
from pages.loan_page import LoanPage

with open("testdata/data.json") as f:
    data = json.load(f)

def test_apply_for_loan(page):
    login = LoginPage(page)
    loan = LoanPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    page.wait_for_timeout(2000)
    loan.go_to_loan(page)
    page.wait_for_timeout(2000)
    loan.apply_for_loan(
        data["loan"]["amount"],
        data["loan"]["down_payment"]
    )
    page.wait_for_timeout(3000)
    result = loan.get_result_heading()
    assert "Loan Request Processed" in result or \
           "Denied" in result