from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.api.dao.models.locations_orm import LocationsOrm
from app.api.dao.repositories.base.base_repository import BaseRepository
from app.api.constants.error_constants import LOCATION_NOT_FOUND_ERROR
from app.api.exceptions.not_found_exception import NotFoundException

class LocationRepository(BaseRepository):
    
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        super.__init__(session_factory, LocationsOrm)
        self.session_factory = session_factory
        
    def get_locations_by_user_id(self, user_id: int) -> Iterator[LocationsOrm]:
        with self.session_factory() as session:
            return (
                session.query(LocationsOrm)
                .filter(LocationsOrm.user_id == user_id)
                .all()
            )
            
    def delete_by_user_id_and_location_name(self, user_id: int, location_name: str) -> None:
        with self.session_factory() as session:
            location = (
                session.query(LocationsOrm)
                .filter(LocationsOrm.user_id == user_id)
                .filter(LocationsOrm.name == location_name)
                .first()
            )
            if not location:
                raise NotFoundException(
                    LOCATION_NOT_FOUND_ERROR.format(
                        entity_class=self.entity_class.__name__,
                        entity_name=location_name,
                        user_id=user_id,
                    )
                )
            session.delete(location)
            session.commit()