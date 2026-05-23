from utilities.base_page import BasePage

class TransferPage(BasePage):
    AMOUNT = "#amount"
    FROM_ACCOUNT = "#fromAccountId"
    TO_ACCOUNT = "#toAccountId"
    TRANSFER_BTN = "input[value='Transfer']"
    SUCCESS_HEADING = "#showResult h1"
    SUCCESS_AMOUNT = "#showResult #amount"

    def go_to_transfer(self, page):
        page.goto(
            "https://parabank.parasoft.com/parabank/transfer.htm"
        )

    def transfer_funds(self, amount):
        self.fill(self.AMOUNT, amount)
        self.click(self.TRANSFER_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_HEADING)