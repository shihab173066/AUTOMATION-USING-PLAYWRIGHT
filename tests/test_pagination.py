from page_objects.employee_page import EmployeePage
from utilities.csv_util import generate_employees_csv

def test_pagination(page):
    emp_page = EmployeePage(page)
    emp_page.goto("https://opensource-demo.orangehrmlive.com/")

    # Login
    page.fill("#txtUsername", "Admin")
    page.fill("#txtPassword", "admin123")
    page.click("#btnLogin")

    # Pagination
    try:
        if page.locator("a#next").is_visible():
            page.click("a#next")
        else:
            print("Page 2 not available, generating CSV...")
            generate_employees_csv()
    except:
        print("Pagination arrow not found")
