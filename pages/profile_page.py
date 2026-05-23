from utilities.base_page import BasePage

class ProfilePage(BasePage):
    FIRST_NAME = "[id='customer.firstName']"
    LAST_NAME = "[id='customer.lastName']"
    ADDRESS = "[id='customer.address.street']"
    CITY = "[id='customer.address.city']"
    STATE = "[id='customer.address.state']"
    ZIP = "[id='customer.address.zipCode']"
    PHONE = "[id='customer.phoneNumber']"
    UPDATE_BTN = "input[value='Update Profile']"
    SUCCESS_MSG = "#updateProfileResult p"

    def go_to_profile(self, page):
        page.goto(
            "https://parabank.parasoft.com/parabank/updateprofile.htm"
        )

    def update_profile(self, data):
        self.page.locator(self.FIRST_NAME).clear()
        self.fill(self.FIRST_NAME, data["first_name"])
        self.page.locator(self.LAST_NAME).clear()
        self.fill(self.LAST_NAME, data["last_name"])
        self.page.locator(self.ADDRESS).clear()
        self.fill(self.ADDRESS, data["address"])
        self.page.locator(self.CITY).clear()
        self.fill(self.CITY, data["city"])
        self.page.locator(self.STATE).clear()
        self.fill(self.STATE, data["state"])
        self.page.locator(self.ZIP).clear()
        self.fill(self.ZIP, data["zip_code"])
        self.page.locator(self.PHONE).clear()
        self.fill(self.PHONE, data["phone"])
        self.click(self.UPDATE_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)