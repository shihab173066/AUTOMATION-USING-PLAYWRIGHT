from page_objects.employee_page import EmployeePage
from utilities.employee_util import generate_employee_id
from utilities.json_util import save_employee_id

def test_add_employee(page):
    emp_page = EmployeePage(page)
    emp_page.goto("https://opensource-demo.orangehrmlive.com/")

    # Login
    page.fill("#txtUsername", "Admin")
    page.fill("#txtPassword", "admin123")
    page.click("#btnLogin")

    # Add Employee
    emp_id = generate_employee_id()
    first_name = f"Test{emp_id}"
    last_name = "User"
    emp_page.add_employee(first_name, last_name)
    save_employee_id(first_name)
    assert page.locator(f"text={first_name}").is_visible()
