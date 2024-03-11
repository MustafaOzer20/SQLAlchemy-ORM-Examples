from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer, 
    String
)
from models.product_categories import ProductCategoryTable

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Diğer özellikler eklenebilir
    categories = relationship("Category", secondary=ProductCategoryTable, back_populates="products")