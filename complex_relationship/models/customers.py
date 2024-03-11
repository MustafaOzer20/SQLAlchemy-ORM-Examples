from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    delivery_address_id = Column(Integer, ForeignKey('addresses.id'))
    billing_address_id = Column(Integer, ForeignKey('addresses.id'))

    orders = relationship("Order", back_populates="customer")
    delivery_address = relationship(
        "Address",
        foreign_keys=[delivery_address_id],
        backref="delivery_customer"
    )
    billing_address = relationship(
        "Address",
        foreign_keys=[billing_address_id],
        backref="billing_customer"
    )
