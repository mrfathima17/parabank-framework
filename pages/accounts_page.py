from utilities.base_page import BasePage

class AccountsPage(BasePage):
    ACCOUNTS_LINK = "a[href*='overview']"
    ACCOUNT_TABLE = "#accountTable"
    ACCOUNT_LINK = "#accountTable tbody tr:first-child td:first-child a"
    ACCOUNT_DETAIL_HEADING = "#rightPanel h1.title >> nth=0"
    AMOUNT = "#amount"
    TRANSFER_BTN = "input[value='Transfer']"
    TRANSFER_SUCCESS = "#showResult h1"

    def go_to_accounts(self):
        self.click(self.ACCOUNTS_LINK)

    def is_account_table_visible(self):
        return self.is_visible(self.ACCOUNT_TABLE)

    def go_to_transfer(self):
        self.click(self.TRANSFER_LINK)

    def transfer_funds(self, amount):
        self.fill(self.AMOUNT, amount)
        self.click(self.TRANSFER_BTN)

    def get_transfer_success_message(self):
        return self.get_text(self.TRANSFER_SUCCESS)

    def click_first_account(self):
        self.click(self.ACCOUNT_LINK)

    def get_account_detail_heading(self):
        return self.get_text(self.ACCOUNT_DETAIL_HEADING)