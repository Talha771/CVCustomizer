
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app import Base

class Experience(Base):
    __tablename__ = 'Experience'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    name = Column(String(255), nullable=False)
    company_name = Column(String(255))
    designation = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    link = Column(String(255))
    stack = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="experience")
