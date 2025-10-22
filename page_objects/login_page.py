from page_objects.base_page import BasePage

class LoginPage(BasePage):
    username_input = "#txtUsername"
    password_input = "#txtPassword"
    login_btn = "#btnLogin"

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_btn)
