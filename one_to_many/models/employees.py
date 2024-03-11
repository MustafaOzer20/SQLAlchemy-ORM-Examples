from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer, 
    String,
    ForeignKey
)

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Department ile Employee arasında one-to-many ilişki
    department = relationship("Department", back_populates="employees")