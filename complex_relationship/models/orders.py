from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_number = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
