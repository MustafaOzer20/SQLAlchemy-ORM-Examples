from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    quantity = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.id'))

    order = relationship("Order", back_populates="order_items")
