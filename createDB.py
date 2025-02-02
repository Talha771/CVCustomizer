from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base
from dotenv import load_dotenv
import os 

from database.models import Education, Experience, Projects, Skills, Subheadings, User
load_dotenv()
DB_URL = os.getenv("DB_URL")
DB_PORT = os.getenv("DB_PORT", "5432")  # Default to 5432 if not set
DB_USERNAME = os.getenv("DB_USERNAME")
DB_SECRET = os.getenv("DB_SECRET")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_SECRET}@{DB_URL}:{DB_PORT}/{DB_NAME}"

print(DATABASE_URL)
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