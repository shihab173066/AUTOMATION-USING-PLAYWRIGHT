1️⃣ pytest.ini (root level)

This file will centralize all Pytest configurations — HTML report path, retries, log level, and markers.

Create a file named pytest.ini inside your root folder:

[pytest]
addopts = --html=playwright-report/report.html --self-contained-html --reruns 1 --maxfail=1
testpaths = tests
log_cli = 1
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)s] %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S

markers =
    smoke: mark test as smoke test
    regression: mark test as regression test
    e2e: mark test as end-to-end scenario

💡 Explanation

--html → automatically generates Playwright report.

--reruns 1 → retries flaky tests once.

--maxfail=1 → stops after one critical failure.

markers → helps you categorize and selectively run tests (pytest -m smoke).

2️⃣ Global Timeout and Retries (playwright.config.py)

Set global timeout and retry behavior for all Playwright actions.

# playwright.config.py
import os
from playwright.sync_api import Playwright, sync_playwright

def pytest_configure(config):
    # Custom hook for Playwright settings
    os.environ["PLAYWRIGHT_GLOBAL_TIMEOUT"] = "15000"  # 15 seconds
    os.environ["PLAYWRIGHT_RETRIES"] = "1"

3️⃣ Utility – Screenshot & Logging Wrapper

Add this file → utilities/playwright_utilities/wrapper.py

import os
import time
from playwright.sync_api import Page

class PlaywrightWrapper:
    def __init__(self, page: Page):
        self.page = page
        self.screenshot_dir = "playwright-report/screenshots"
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def click(self, selector, name="element"):
        try:
            self.page.click(selector)
        except Exception as e:
            self._capture_error(name, e)

    def fill(self, selector, value, name="input"):
        try:
            self.page.fill(selector, value)
        except Exception as e:
            self._capture_error(name, e)

    def goto(self, url):
        try:
            self.page.goto(url)
        except Exception as e:
            self._capture_error("navigation", e)

    def _capture_error(self, action_name, error):
        filename = f"{self.screenshot_dir}/{action_name}_{int(time.time())}.png"
        self.page.screenshot(path=filename)
        raise Exception(f"[Playwright Error] {action_name} failed: {error}. Screenshot: {filename}")


✅ This ensures:

Every failed action gets a screenshot.

You can trace logs and screenshots in CI/CD artifacts.

4️⃣ Automatic Screenshot Folder Creation

Add this snippet to your conftest.py in the project root (Pytest automatically detects it):

import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_directories():
    os.makedirs("playwright-report/screenshots", exist_ok=True)

5️⃣ CSV Generator for Pagination Test

Add this file → utilities/csv_generator.py

import csv

def generate_employee_csv(file_path="tests/data/employees.csv", count=50):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["FirstName", "LastName", "Email", "JobTitle"])
        for i in range(count):
            writer.writerow([f"First{i}", f"Last{i}", f"first{i}@example.com", "QA Engineer"])
    print(f"✅ CSV generated with {count} employees at {file_path}")


You can call it in your pagination test when needed:

from utilities.csv_generator import generate_employee_csv
generate_employee_csv()

✅ Now Your Framework Has
Component	Purpose
pytest.ini	Central config for reports, retries, and markers
playwright.config.py	Global timeout and retry settings
wrapper.py	Error-handled Playwright actions with screenshots
conftest.py	Auto folder setup for reports
csv_generator.py	Dynamic data generation for pagination
playwright.yml	CI/CD workflow with parallel execution
Monocart / HTML report	Centralized execution reporting

Next, I can help you build:

A data_manager.py to handle JSON save/read for Step 7 (Employee ID sharing between tests).

And an example test file (test_add_employee.py) fully implemented with POM, JSON writing, and wrappers.
done