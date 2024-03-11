from database import Base
from sqlalchemy import Column, Integer, String


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    postal_code = Column(String)
