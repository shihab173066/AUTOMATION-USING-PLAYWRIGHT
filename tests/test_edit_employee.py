from page_objects.employee_page import EmployeePage
from utilities.json_util import read_employee_id

def test_edit_employee(page):
    emp_page = EmployeePage(page)
    emp_page.goto("https://opensource-demo.orangehrmlive.com/")

    # Login
    page.fill("#txtUsername", "Admin")
    page.fill("#txtPassword", "admin123")
    page.click("#btnLogin")

    emp_name = read_employee_id()
    emp_page.search_employee(emp_name)
    page.click(f"xpath=//a[text()='{emp_name}']")
    page.fill("#personal_txtEmpFirstName", emp_name+"_Edited")
    page.click("#btnSave")
    assert page.locator(f"text={emp_name}_Edited").is_visible()
