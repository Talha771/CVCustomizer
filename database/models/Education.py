
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app import Base

class Education(Base):
    __tablename__ = 'Education'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    name = Column(String(255), nullable=False)
    institution_name = Column(String(255), nullable=False)
    type_of_education = Column(ENUM('High School', 'BSc', 'MSc', 'PhD', 'Diploma', name='education_type'), nullable=False)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer)
    grade = Column(String(50))
    
    # Relationships
    user = relationship("User", back_populates="education")

