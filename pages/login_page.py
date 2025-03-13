from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = "//input[@id='user-name']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='login-button']"

    def login(self, username, password):
        """Logs into the application"""
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
