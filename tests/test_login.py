from page_objects.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.goto("https://opensource-demo.orangehrmlive.com/")
    login_page.login("Admin", "admin123")
    assert page.locator("#welcome").is_visible()
