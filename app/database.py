from sqlmodel import SQLModel, Session, create_engine

from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def create_db_and_tables():
    """
    Create database tables during application startup.
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """
    Provide database sessions through dependency injection.
    """
    with Session(engine) as session:
        yield session