from utilities.base_page import BasePage

class BillPayPage(BasePage):
    PAYEE_NAME = "input[name='payee.name']"
    ADDRESS = "input[name='payee.address.street']"
    CITY = "input[name='payee.address.city']"
    STATE = "input[name='payee.address.state']"
    ZIP = "input[name='payee.address.zipCode']"
    PHONE = "input[name='payee.phoneNumber']"
    ACCOUNT = "input[name='payee.accountNumber']"
    VERIFY_ACCOUNT = "input[name='verifyAccount']"
    AMOUNT = "input[name='amount']"
    FROM_ACCOUNT = "select[name='fromAccountId']"
    SEND_BTN = "input[value='Send Payment']"
    SUCCESS_HEADING = "#billpayResult h1"

    def go_to_billpay(self, page):
        page.goto(
            "https://parabank.parasoft.com/parabank/billpay.htm"
        )

    def pay_bill(self, data):
        self.fill(self.PAYEE_NAME, data["payee_name"])
        self.fill(self.ADDRESS, data["address"])
        self.fill(self.CITY, data["city"])
        self.fill(self.STATE, data["state"])
        self.fill(self.ZIP, data["zip_code"])
        self.fill(self.PHONE, data["phone"])
        self.fill(self.ACCOUNT, data["account_number"])
        self.fill(self.VERIFY_ACCOUNT, data["account_number"])
        self.fill(self.AMOUNT, data["amount"])
        self.click(self.SEND_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_HEADING)