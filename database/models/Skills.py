
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app import Base

class Skills(Base):
    __tablename__ = 'Skills'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    name = Column(String(255), nullable=False)
    languages = Column(String(255))
    tools = Column(String(255))
    
    # Relationships
    user = relationship("User", back_populates="skills")
