import csv
from utilities.employee_util import generate_employee_id

def generate_employees_csv(filename="data/employees.csv", count=50):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Employee ID"])
        for _ in range(count):
            emp_id = generate_employee_id()
            writer.writerow([f"Test{emp_id}", "User", emp_id])
