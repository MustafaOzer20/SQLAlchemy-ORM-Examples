from models import (
    Department,
    Employee
)
from database import Session, Base, engine



Base.metadata.create_all(engine)

# Oturumu oluştur
session = Session()

# Departmanlar ve çalışanları oluştur
hr_department = Department(name='Human Resources')
it_department = Department(name='Information Technology')

employee1 = Employee(name='John', department=hr_department)
employee2 = Employee(name='Alice', department=it_department)
employee3 = Employee(name='Bob', department=it_department)

# Oturuma ekle ve değişiklikleri kaydet
session.add_all([hr_department, it_department, employee1, employee2, employee3])
session.commit()

# Oturumu kapat
session.close()