from models import (
    Department,
    Employee
)
from database import Session


def department_to_employee():
    session = Session()
    
    it_department = session.query(Department).filter_by(name='Information Technology').first()
    it_employees = it_department.employees
    for employee in it_employees:
        print({
            "Department": "IT",
            "Employee": employee.name
        })

    session.close()


def employee_to_department():
    session = Session()
    
    employees = session.query(Employee).all()
    for employee in employees:
        print({
            "Department": employee.department.name,
            "Employee": employee.name
        })

    session.close()


def main():
    department_to_employee()
    print(50*"-")
    employee_to_department()


if __name__ == "__main__":
    main()