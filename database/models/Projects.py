
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app import Base

class Projects(Base):
    __tablename__ = 'Projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    stack = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    link = Column(String(255))
    
    # Relationships
    user = relationship("User", back_populates="projects")
