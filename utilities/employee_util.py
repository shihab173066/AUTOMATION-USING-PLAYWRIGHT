from datetime import datetime
import random

def generate_employee_id():
    return f"EMP{datetime.utcnow().strftime('%Y%m%d%H%M%S')}{random.randint(100,999)}"
