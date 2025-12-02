from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.api.constants.error_constants import ENTITY_ID_NOT_FOUND_ERROR
from app.api.exceptions.not_found_exception import NotFoundException


class BaseRepository:
    
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
        entity_class: object, 
    ) -> None:
        self.session_factory = session_factory
        self.entity_class = entity_class
        
    def get_all(self) -> Iterator[object]:
        with self.session_factory() as session:
            return session.query(self.entity_class).all()
        
    def get_by_id(self, entity_id: int) -> object:
        with self.session_factory() as session:
            entity = (
                session.query(self.entity_class)
                .filter(self.entity_class.id == entity_id)
                .first()
            )
            if not entity:
                raise NotFoundException(
                    ENTITY_ID_NOT_FOUND_ERROR.format(
                        entity_name=self.entity_class.__name__,
                        entity_id=entity_id,
                    )
                )
            return entity
        
    def add(self, entity: object) -> object:
        with self.session_factory() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity
        
    def update(self, entity_id: int, entity: object) -> object:
        with self.session_factory() as session:
            entity.id = entity_id
            session.merge(entity)
            session.commit()
            return self.get_by_id(entity_id)
        
    def delete_by_id(self, entity_id: int) -> None:
        with self.session_factory() as session:
            entity = (
                session.query(self.entity_class)
                .filter(self.entity_class.id == entity_id)
                .first()
            )
            if not entity:
                raise NotFoundException(
                    ENTITY_ID_NOT_FOUND_ERROR.format(
                        entity_class=self.entity_class.__name__,
                        entity_id=entity_id,
                    )
                )
            session.delete(entity)
            session.commit()