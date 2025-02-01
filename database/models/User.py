from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app import Base

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(15))
    github = Column(String(255))
    linkedin = Column(String(255))
    number = Column(String(15))
    password_hash = Column(Text, nullable=False)
    
    # Relationships
    education = relationship("Education", back_populates="user")
    experience = relationship("Experience", back_populates="user")
    projects = relationship("Projects", back_populates="user")
    skills = relationship("Skills", back_populates="user")
