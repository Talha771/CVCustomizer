
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app import Base

class SubHeadings(Base):
    __tablename__ = 'SubHeadings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description_type = Column(ENUM('experience', 'project', name='description_type'), nullable=False)
    experience_id = Column(Integer, ForeignKey('Experience.id'))
    project_id = Column(Integer, ForeignKey('Projects.id'))
    bullet_point_1 = Column(Text)
    bullet_point_2 = Column(Text)
    bullet_point_3 = Column(Text)
    
    # Relationships
    experience = relationship("Experience")
    project = relationship("Projects")
