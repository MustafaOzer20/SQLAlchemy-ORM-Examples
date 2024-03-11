from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer, 
    String, 
    ForeignKey
)

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Profile ile User arasında one-to-one ilişki
    user = relationship("User", back_populates="profile")