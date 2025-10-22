import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session", autouse=True)
def create_screenshot_folder():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
