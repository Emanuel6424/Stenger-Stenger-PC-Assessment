from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection string (adjust for your setup)
DATABASE_URL = "postgresql://postgres:6424123@localhost/phonebook"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(bind=engine)

# Base class for database models
Base = declarative_base()

# Function to get a database session


def get_db():
    database_session = SessionLocal()
    try:
        yield database_session  # Provide session to the request
    finally:
        database_session.close()  # Close session after request
