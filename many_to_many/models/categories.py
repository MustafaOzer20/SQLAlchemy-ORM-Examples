from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer, 
    String
)
from models.product_categories import ProductCategoryTable

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Diğer özellikler eklenebilir
    products = relationship("Product", secondary=ProductCategoryTable, back_populates="categories")