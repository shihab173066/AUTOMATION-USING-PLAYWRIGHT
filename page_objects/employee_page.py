from page_objects.base_page import BasePage

class EmployeePage(BasePage):
    add_btn = "#btnAdd"
    first_name_input = "#firstName"
    last_name_input = "#lastName"
    save_btn = "#btnSave"
    emp_list_table = "#resultTable"

    def add_employee(self, first_name, last_name):
        self.page.click(self.add_btn)
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.click(self.save_btn)

    def search_employee(self, emp_name):
        self.page.fill("#empsearch_employee_name_empName", emp_name)
        self.page.click("#searchBtn")
