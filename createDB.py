from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base

from database.models import Education, Experience, Projects, Skills, Subheadings, User

DATABASE_URL = "postgresql://postgres:talha1205@localhost:5432/CV"

def db_init():
    for table in Base.metadata.tables.values():
        print(f"Table: {table.name}")
        for column in table.columns:
            print(f"  Column: {column.name}, Type: {column.type}")
    print("Initializing database...")
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")
    
db_init()