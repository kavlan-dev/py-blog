from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from py_blog.models.post import Base


def init_db(database_url: str) -> Session:
    """Initialize the database with all tables."""
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session()
