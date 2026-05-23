from utilities.base_page import BasePage

class RegisterPage(BasePage):
    FIRST_NAME = "[id='customer.firstName']"
    LAST_NAME = "[id='customer.lastName']"
    ADDRESS = "[id='customer.address.street']"
    CITY = "[id='customer.address.city']"
    STATE = "[id='customer.address.state']"
    ZIP = "[id='customer.address.zipCode']"
    PHONE = "[id='customer.phoneNumber']"
    SSN = "[id='customer.ssn']"
    USERNAME = "[id='customer.username']"
    PASSWORD = "[id='customer.password']"
    CONFIRM = "[id='repeatedPassword']"
    REGISTER_BTN = "input[value='Register']"
    SUCCESS_MSG = "#rightPanel"

    def register(self, data):
        self.fill(self.FIRST_NAME, data["first_name"])
        self.fill(self.LAST_NAME, data["last_name"])
        self.fill(self.ADDRESS, data["address"])
        self.fill(self.CITY, data["city"])
        self.fill(self.STATE, data["state"])
        self.fill(self.ZIP, data["zip_code"])
        self.fill(self.PHONE, data["phone"])
        self.fill(self.SSN, data["ssn"])
        self.fill(self.USERNAME, data["username"])
        self.fill(self.PASSWORD, data["password"])
        self.fill(self.CONFIRM, data["password"])
        self.click(self.REGISTER_BTN)

    def register_with_mismatched_password(self, data, wrong_confirm):
        self.fill(self.FIRST_NAME, data["first_name"])
        self.fill(self.LAST_NAME, data["last_name"])
        self.fill(self.ADDRESS, data["address"])
        self.fill(self.CITY, data["city"])
        self.fill(self.STATE, data["state"])
        self.fill(self.ZIP, data["zip_code"])
        self.fill(self.PHONE, data["phone"])
        self.fill(self.SSN, data["ssn"])
        self.fill(self.USERNAME, data["username"])
        self.fill(self.PASSWORD, data["password"])
        self.fill(self.CONFIRM, wrong_confirm)
        self.click(self.REGISTER_BTN)