from database import Base
from sqlalchemy import (
    Table,
    Column,
    Integer, 
    ForeignKey
)

ProductCategoryTable = Table('product_category', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)