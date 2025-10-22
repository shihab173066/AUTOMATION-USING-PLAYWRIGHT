import json

def save_employee_id(emp_id, filename="data/employee.json"):
    with open(filename, "w") as f:
        json.dump({"employee_id": emp_id}, f)

def read_employee_id(filename="data/employee.json"):
    with open(filename, "r") as f:
        return json.load(f)["employee_id"]
