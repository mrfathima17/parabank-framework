from utilities.base_page import BasePage

class FindTransactionPage(BasePage):
    ACCOUNT_DROPDOWN = "#accountId"
    SEARCH_BY_AMOUNT = "#amount"
    FIND_BY_AMOUNT_BTN = "#findByAmount"
    SEARCH_BY_DATE = "#transactionDate"
    FIND_BY_DATE_BTN = "#findByDate"
    RESULTS_TABLE = "#transactionTable"

    def go_to_find_transactions(self, page):
        page.goto(
            "https://parabank.parasoft.com/parabank/findtrans.htm"
        )

    def search_by_amount(self, amount):
        self.fill(self.SEARCH_BY_AMOUNT, amount)
        self.click(self.FIND_BY_AMOUNT_BTN)

    def search_by_date(self, date):
        self.fill(self.SEARCH_BY_DATE, date)
        self.click(self.FIND_BY_DATE_BTN)

    def is_results_table_visible(self):
        return self.is_visible(self.RESULTS_TABLE)