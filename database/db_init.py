from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base

DB_USER = "postgres"
DB_PASSWORD = "talha1205"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port
DB_NAME = "CV"

# PostgreSQL connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def db_init():# Importing Base here to create tables
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    "I have run"
db_init()