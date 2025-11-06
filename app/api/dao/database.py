from sqlalchemy.orm import DeclarativeBase, Session
from contextlib import contextmanager, AbstractContextManager
from collections.abc import Callable
from sqlalchemy import create_engine, orm 
from sqlalchemy_utils import database_exists, create_database

from app.api.settings.datasource_settings import DatasourceSettings

class Base(DeclarativeBase):
    pass


class Database:

    def __init__(self, datasource_settings: DatasourceSettings) -> None:
        self._config = datasource_settings
        self._engine = create_engine(self._config.url, echo=True)
        self._session_factory = orm.sessionmaker(
            autocommit=False,
            autoflush=False, 
            bind=self._engine,
        )

    def create_db(self) -> None:
        if not database_exists(self._engine.url):
            create_database(self._engine.url)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    