from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Replace these with your actual PostgreSQL credentials
DB_USER = "postgres"
DB_PASSWORD = "talha1205"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port
DB_NAME = "postgres"

# PostgreSQL connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
def db_connect():
    SessionLocal = sessionmaker(bind=engine)

    # Base class for ORM models
    session = SessionLocal()
    from sqlalchemy import text

    # Initialize the session
    session = SessionLocal()

    try:
        # Execute a simple query to test the connection
        result = session.execute(text("SELECT 1"))  # Wrap the query in text()
        
        # Check the result
        if result.rowcount > 0:
            print("Connection successful!")
        else:
            print("Connection test returned no results.")
        
    except Exception as e:
        # If there is an error, print the error message
        print(f"An error occurred: {e}")
