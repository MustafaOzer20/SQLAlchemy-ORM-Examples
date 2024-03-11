from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer, 
    String
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # User ile Profile arasında one-to-one ilişki
    profile = relationship("Profile", uselist=False, back_populates="user")