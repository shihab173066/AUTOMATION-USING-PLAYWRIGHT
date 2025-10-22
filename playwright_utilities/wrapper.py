from playwright.sync_api import Page
import time
import os

class PlaywrightWrapper:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        try:
            self.page.locator(locator).click()
        except Exception as e:
            print(f"Click failed on {locator}: {e}")
            self.page.screenshot(path=f"screenshots/click_error_{int(time.time())}.png")
            raise

    def fill(self, locator, text):
        try:
            self.page.locator(locator).fill(text)
        except Exception as e:
            print(f"Fill failed on {locator}: {e}")
            self.page.screenshot(path=f"screenshots/fill_error_{int(time.time())}.png")
            raise

    def goto(self, url):
        try:
            self.page.goto(url)
        except Exception as e:
            print(f"Goto failed for {url}: {e}")
            self.page.screenshot(path=f"screenshots/goto_error_{int(time.time())}.png")
            raise
