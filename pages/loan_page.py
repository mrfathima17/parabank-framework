from utilities.base_page import BasePage

class LoanPage(BasePage):
    LOAN_AMOUNT = "#amount"
    DOWN_PAYMENT = "#downPayment"
    APPLY_BTN = "input[value='Apply Now']"
    RESULT_HEADING = "#requestLoanResult h1"
    LOAN_PROVIDER = "#loanRequestResults p"

    def go_to_loan(self, page):
        page.goto(
            "https://parabank.parasoft.com/parabank/requestloan.htm"
        )

    def apply_for_loan(self, amount, down_payment):
        self.fill(self.LOAN_AMOUNT, amount)
        self.fill(self.DOWN_PAYMENT, down_payment)
        self.click(self.APPLY_BTN)

    def get_result_heading(self):
        return self.get_text(self.RESULT_HEADING)