from page_objects.employee_page import EmployeePage
from utilities.json_util import read_employee_id

def test_delete_employee(page):
    emp_page = EmployeePage(page)
    emp_page.goto("https://opensource-demo.orangehrmlive.com/")

    # Login
    page.fill("#txtUsername", "Admin")
    page.fill("#txtPassword", "admin123")
    page.click("#btnLogin")

    emp_name = read_employee_id()
    emp_page.search_employee(emp_name)
    page.check(f"xpath=//a[text()='{emp_name}']/../..//input[@type='checkbox']")
    page.click("#btnDelete")
    page.click("#dialogDeleteBtn")
    assert not page.locator(f"text={emp_name}").is_visible()
