from utilities.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BTN = "input[type='submit']"
    ERROR_MSG = "#rightPanel p.error"
    LOGOUT_LINK = "a[href*='logout']"

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def is_logged_in(self):
        return self.page.url.__contains__("overview")