from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os 
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")
DB_PORT = os.getenv("DB_PORT", "5432")  # Default to 5432 if not set
DB_USERNAME = os.getenv("DB_USERNAME")
DB_SECRET = os.getenv("DB_SECRET")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_SECRET}@{DB_URL}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

def db_connect():
    SessionLocal = sessionmaker(bind=engine)

    session = SessionLocal()
    from sqlalchemy import text

    session = SessionLocal()

    try:
        result = session.execute(text("SELECT 1")) 
        if result.rowcount > 0:
            print("Connection successful!")
        else:
            print("Connection test returned no results.")
        
    except Exception as e:
        # If there is an error, print the error message
        print(f"An error occurred: {e}")
