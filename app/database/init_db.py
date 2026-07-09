from app.database.base import Base
from app.database.models.audio import Audio  # noqa: F401
from app.database.session import engine


def init_db() -> None:
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)